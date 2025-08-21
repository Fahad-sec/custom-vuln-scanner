# custom-vuln-scanner
A custom-built vulnerability scanner to deep dive into learning networking, fingerprinting, CVE lookups, and Cyber-sec tool development.

```

## Project Structure:
➜  custom-vuln-scanner tree              
.
├── cli.py
├── logs
│   └── scanner.log
├── requirements.txt
├── results
│   ├── scan..json
├── scanner
│   ├── core.py
│   ├── fingerprint.py
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── logger.py
│   ├── modules
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── scan_ftp.cpython-313.pyc
│   │   │   ├── scan_http.cpython-313.pyc
│   │   │   └── scan_ssh.cpython-313.pyc
│   │   ├── scan_ftp.py
│   │   ├── scan_http.py
│   │   └── scan_ssh.py
│   ├── __pycache__
│   │   ├── core.cpython-313.pyc
│   │   ├── fingerprint.cpython-313.pyc
│   │   ├── __init__.cpython-313.pyc
│   │   ├── logger.cpython-313.pyc
│   │   ├── results.cpython-313.pyc
│   │   └── vuln_lookup.cpython-313.pyc
│   ├── results.py
│   └── vuln_lookup.py
└── web_ui
    └── app.py
```

## cli.py:
It is the brain of the scanner which helps running all the functions of the scanner with one command. e.g: python2 cli.py example.com
