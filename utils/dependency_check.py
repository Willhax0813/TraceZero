# utils/dependency_check.py

import shutil
import subprocess
import sys

REQUIRED_TOOLS = [
    "assetfinder",
    "subfinder",
    "nmap",
    "whatweb",
    "dirsearch"
]


def check_and_install_dependencies(logger):
    logger.info("[~] Checking dependencies...")
    for tool in REQUIRED_TOOLS:
        if shutil.which(tool) is None:
            logger.warning(f"[!] {tool} not found. Attempting to install...")
            try:
                if tool == "dirsearch":
                    install_dirsearch(logger)
                else:
                    subprocess.run(["go", "install", f"github.com/tomnomnom/{tool}@latest"], check=True)
                    logger.info(f"[+] Installed: {tool}")
            except Exception as e:
                logger.error(f"[x] Failed to install {tool}: {str(e)}")
                sys.exit(1)
        else:
            logger.debug(f"[✓] Found: {tool}")
    logger.info("[✓] All dependencies are satisfied.")


def install_dirsearch(logger):
    import os
    if not os.path.exists("/opt/dirsearch"):
        subprocess.run(["git", "clone", "https://github.com/maurosoria/dirsearch.git", "/opt/dirsearch"], check=True)
        logger.info("[+] Cloned dirsearch to /opt/dirsearch")
    else:
        logger.info("[~] Dirsearch already exists at /opt/dirsearch")

    # Optional: setup alias or check Python dep install if needed
