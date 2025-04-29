# scanner/dir_enum.py

import subprocess
import os
from config import settings


def run(logger):
    target = input("[?] Enter full target URL (with http/https): ").strip()
    output_dir = os.path.join(settings.OUTPUT_DIR, target.replace("https://", "").replace("http://", ""))
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "dir_enum.txt")

    dirsearch_path = settings.TOOL_PATHS.get("dirsearch", "/opt/dirsearch/dirsearch.py")

    logger.info("[+] Running Dirsearch for content discovery...")
    try:
        subprocess.run([
            "python3", dirsearch_path,
            "-u", target,
            "-e", "php,html,js",
            "-w", settings.WORDLIST_PATH,
            "--plain-text-report", out_file
        ], stderr=subprocess.DEVNULL)
        logger.info(f"[✓] Directory enumeration saved to: {out_file}")
    except Exception as e:
        logger.error(f"[x] Dirsearch failed: {e}")