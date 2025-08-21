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
│   ├── *.json #scan results are strored here 
├── scanner
│   ├── core.py
│   ├── fingerprint.py
│   ├── __init__.py
│   ├── logger.py
│   ├── modules
│   │   ├── scan_ftp.py
│   │   ├── scan_http.py
│   │   └── scan_ssh.py
│   ├── results.py
│   └── vuln_lookup.py
└── web_ui
    └── app.py
```

## cli.py:
It is the brain of the scanner which helps running all the functions of the scanner with one command. e.g: python3 cli.py example.com
