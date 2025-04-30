# config/settings.py

import os
import platform
import shutil  # penting! untuk TOOL_PATHS yang pakai shutil.which()

# Default (fallback) paths
TOOL_PATHS = {
    "assetfinder": shutil.which("assetfinder") or "/usr/bin/assetfinder",
    "subfinder": shutil.which("subfinder") or "/usr/bin/subfinder",
    "amass": shutil.which("amass") or "/usr/bin/amass",
    "nmap": shutil.which("nmap") or "/usr/bin/nmap",
    "whatweb": shutil.which("whatweb") or "/usr/bin/whatweb",
    "rustscan": shutil.which("rustscan") or f"{os.path.expanduser('~')}/.cargo/bin/rustscan",
    "dirsearch": shutil.which("dirsearch") or "/opt/dirsearch/dirsearch.py",
}

LOG_LEVEL = "INFO"
OUTPUT_DIR = "output/"
