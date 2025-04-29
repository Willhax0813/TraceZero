# config/settings.py

# Mode scanning yang tersedia: light, deep, stealth
SCAN_MODE = "light"  # bisa diganti menjadi "deep" atau "stealth"

# Gunakan proxy untuk mode stealth
USE_PROXY = True

# Default wordlist path (bisa diganti sesuai kebutuhan)
WORDLIST_PATH = "wordlists/common.txt"

# Path tools eksternal jika tidak ada di PATH environment
TOOL_PATHS = {
    "assetfinder": "/usr/bin/assetfinder",
    "subfinder": "/usr/bin/subfinder",
    "amass": "/usr/bin/amass",
    "nmap": "/usr/bin/nmap",
    "whatweb": "/usr/bin/whatweb",
    "dirsearch": "/tools/dirsearch/dirsearch.py"
}

# API Keys (jika dibutuhkan oleh modul tertentu)
API_KEYS = {
    "intelx": "YOUR_INTELX_KEY",
    "shodan": "YOUR_SHODAN_KEY",
    "wappalyzer": "YOUR_WAPPALYZER_KEY"
}

# Rate limit global (untuk future proxy rotator / stealth mode)
RATE_LIMIT = 2  # request per detik

# Logging level: DEBUG, INFO, WARNING, ERROR
LOG_LEVEL = "INFO"

# Output directory
OUTPUT_DIR = "output/"

# Save format
EXPORT_FORMAT = ["html", "json"]