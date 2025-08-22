import re 
import requests 

def parse_service_version(banner):
    """
    Extract service name and version from banner.
    Example: '220 (vsFTPd 3.0.3)' -> ('vsftpd', '3.0.3)
    """
    match = re.search(r'([a-zA-Z\-]+)[/ ]?([0-9]+(\.[0-9]+)?)?', banner)
    if match:
        service = match.group(1).lower()
        version = match.group(2) if match.group(2) else None
        return service, version
    return None, None

def lookup_cve(service, version=None):
    """
    Query CIRCL CVE API for vulnerabilities.
    Always returns a list (empty if none found or error).
    """
    if not service:
        return []

    base_url = f"https://cve.circl.lu/api/search/{service}"
    if version:
        base_url += f"/{version}"

    print(f"[+] Quering CVE database for {service} {version or ''}...")
    try:
        resp = requests.get(base_url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, dict) and 'results' in data:
                return data['results']
            elif isinstance(data, list):
                return data
        else:
            print(f"[-] CVE API request failed:HTTP {resp.status_code}")
        return []

    except Exception as e:
        print(f"[-] Error quering CVE API: {e}")
    return []

