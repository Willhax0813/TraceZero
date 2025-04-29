# utils/dependency_check.py

import shutil
import subprocess
import sys
import os

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
        if shutil.which(tool) is None and tool != "dirsearch":
            logger.warning(f"[!] {tool} not found. Attempting to install...")
            try:
                subprocess.run(["go", "install", f"github.com/tomnomnom/{tool}@latest"], check=True)
                logger.info(f"[+] Installed: {tool}")
            except Exception as e:
                logger.error(f"[x] Failed to install {tool}: {str(e)}")
                sys.exit(1)
        elif tool == "dirsearch":
            install_dirsearch(logger)
        else:
            logger.debug(f"[✓] Found: {tool}")
    logger.info("[✓] All dependencies are satisfied.")# utils/dependency_check.py

import shutil
import subprocess
import sys
import os

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
        if shutil.which(tool) is None and tool != "dirsearch":
            logger.warning(f"[!] {tool} not found. Attempting to install...")
            try:
                subprocess.run(["go", "install", f"github.com/tomnomnom/{tool}@latest"], check=True)
                logger.info(f"[+] Installed: {tool}")
            except Exception as e:
                logger.error(f"[x] Failed to install {tool}: {str(e)}")
                sys.exit(1)
        elif tool == "dirsearch":
            install_dirsearch(logger)
        else:
            logger.debug(f"[✓] Found: {tool}")
    logger.info("[✓] All dependencies are satisfied.")


def install_dirsearch(logger):
    dirsearch_dir = os.path.join(os.getcwd(), "tools", "dirsearch")
    if not os.path.exists(dirsearch_dir):
        os.makedirs(os.path.dirname(dirsearch_dir), exist_ok=True)
        subprocess.run(["git", "clone", "https://github.com/maurosoria/dirsearch.git", dirsearch_dir], check=True)
        logger.info(f"[+] Cloned dirsearch to {dirsearch_dir}")
    else:
        logger.info(f"[~] Dirsearch already exists at {dirsearch_dir}")