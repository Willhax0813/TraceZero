# scanner/portscan.py

import subprocess
import os
from config import settings


def run_light(logger):
    target = input("[?] Enter IP/domain for port scan: ").strip()
    output_dir = os.path.join(settings.OUTPUT_DIR, target)
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "light_portscan.txt")

    logger.info("[+] Running Rustscan (light scan)...")
    try:
        subprocess.run(["rustscan", "-a", target, "--ulimit", "5000", "-g"], stdout=open(out_file, "w"), stderr=subprocess.DEVNULL)
        logger.info(f"[✓] Light port scan saved to: {out_file}")
    except Exception as e:
        logger.error(f"[x] Rustscan failed: {e}")


def run_deep(logger):
    target = input("[?] Enter IP/domain for deep scan: ").strip()
    output_dir = os.path.join(settings.OUTPUT_DIR, target)
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "deep_portscan.txt")

    logger.info("[+] Running Nmap (deep scan)...")
    try:
        subprocess.run(["nmap", "-sC", "-sV", "-T4", "-Pn", target], stdout=open(out_file, "w"), stderr=subprocess.DEVNULL)
        logger.info(f"[✓] Deep port scan saved to: {out_file}")
    except Exception as e:
        logger.error(f"[x] Nmap deep scan failed: {e}")


def run_stealth(logger):
    target = input("[?] Enter IP/domain for stealth scan: ").strip()
    output_dir = os.path.join(settings.OUTPUT_DIR, target)
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "stealth_portscan.txt")

    logger.info("[~] Running Nmap in stealth mode...")
    try:
        subprocess.run(["nmap", "-sS", "-T2", "-Pn", target], stdout=open(out_file, "w"), stderr=subprocess.DEVNULL)
        logger.info(f"[✓] Stealth port scan saved to: {out_file}")
    except Exception as e:
        logger.error(f"[x] Nmap stealth scan failed: {e}")
