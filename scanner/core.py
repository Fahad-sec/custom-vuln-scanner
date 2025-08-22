import socket
import importlib

from scanner import fingerprint, vuln_lookup, logger
from scanner import results as results_writer

PORT_MODULE_MAP = {
    80: "scan_http",
    22: "scan_ssh",
    21: "scan_ftp",   

}

def scan_host(host, ports, timeout=1):
    """
    Do a TCP connect scan, banner-grab, run protocol modules, lookup CVEs,
    and save results to results/ as JSON.
    """
    logger.log(f"Starting scan on {host}")
    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            open_ports.append(port)
            logger.log(f"[+] Port {port} is open")
        except Exception:
            pass
        finally:
            sock.close()

    logger.log(f"[+] Scan complete. open ports: {open_ports}")

    banners = {}
    module_outputs = {}
    vulns_found = []

    for port in open_ports:
        banner = fingerprint.grab_banner(host, port)
        if banner:
            banners[str(port)] = banner

            try:
                svc, ver = vuln_lookup.parse_service_version(banner)
                if svc:
                    hits = vuln_lookup.lookup_cve(svc, ver)
                    if hits:
                        vulns_found.extend(hits)
            except Exception as e:
                logger.log(f"[!] vuln lookup error for {host}:{port} -> {e}")

        if port in PORT_MODULE_MAP:
            out = run_module(PORT_MODULE_MAP[port], host, port)
            if out is not None:
                module_outputs[str(port)] = out

    scan_result = {
        "target": host,
        "open_ports": open_ports,
        "banners": banners,
        "module_outputs": module_outputs,
        "vulnerabilities_count": len(vulns_found),
        "vulnerabilities": [
            {"id": v.get("id"), "summary": v.get("summary")} for v in vulns_found
        ],
    }

    path = results_writer.save_json(scan_result, filename_prefix="scan")
    logger.log(f"[+] Saved scan results to {path}")

    return scan_result

def run_module(module_name, host, port):
    """
    Import and run a module from scanner.modules.<module_name>.
    The module is expected to expose a function with the same name
    (e.g., scanner.modules.scan_http.scan_http(host, port))
    and to return something (dict/list/string) or None.
    """
    try:
        module_path = f"scanner.modules.{module_name}"
        module = importlib.import_module(module_path)
        func = getattr(module, module_name, None)
        if callable(func):
            logger.log(f"[+] Running module {module_name} for {host}:{port}")
            return func(host, port)
        else:
            logger.log(f"[!] Module {module_name} missing entry function {module_name}")
    except Exception as e:
        logger.log(f"[!] Failed to run module {module_name}: {e}")
    return None







