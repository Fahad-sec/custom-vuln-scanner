import sys
from scanner.core import scan_host

DEFAULT_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389]

def usage():
    print("Usage: python3 cli.py <target> [comma-separated-ports]")
    print("Example: python3 cli.py scanme.nmap.org 22,80,443")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    target = sys.argv[1]

    if len(sys.argv) >= 3:
        ports = [int(p.strip()) for p in sys.argv[2].split(",") if p.strip()>
    else:
        ports = DEFAULT_PORTS

    scan_host(target, ports)

