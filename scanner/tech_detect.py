# scanner/tech_detect.py

import subprocess
import os
from config import settings


def run(logger):
    target = input("[?] Enter target domain (with http/https): ").strip()
    output_dir = os.path.join(settings.OUTPUT_DIR, target.replace("https://", "").replace("http://", ""))
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "tech_detect.txt")

    whatweb_path = settings.TOOL_PATHS.get("whatweb", "whatweb")

    logger.info("[+] Running WhatWeb for technology detection...")
    try:
        with open(out_file, "w") as f:
            subprocess.run([whatweb_path, target], stdout=f, stderr=subprocess.DEVNULL)
        logger.info(f"[✓] Tech detection saved to: {out_file}")
    except Exception as e:
        logger.error(f"[x] WhatWeb scan failed: {e}")
