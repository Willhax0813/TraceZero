# main.py

from banner.banner import banner_tracezero_ascii
from rich.console import Console
from utils.dependency_check import check_and_install_dependencies
from scanner import subdomain_enum, portscan, tech_detect, dir_enum
from report.logger import init_logger
from modules.auto_light import auto_light_scan
from config.settings import LOG_LEVEL, OUTPUT_DIR

import sys
import os

console = Console()

def main():
    # Tampilkan banner
    banner_tracezero_ascii()

    # Inisialisasi logger
    logger = init_logger()
    logger.info("[+] Starting TRACEZERO")

    # Auto check & install dependency
    check_and_install_dependencies(logger)

    # Pilihan mode scanning dinamis
    logger.info("[?] Enter your target domain:" )
    domain = input("> ").strip()

    logger.info("[?] Choose scan mode:")
    console.print("[cyan]1.[/] Auto Light Scan")
    console.print("[cyan]2.[/] Deep Scan")
    console.print("[cyan]3.[/] Stealth Scan")
    mode = input("> ").strip()

    if mode == "1":
        logger.info("[~] Running Auto Light Scan mode")
        auto_light_scan.main_target(domain, logger)

    elif mode == "2":
        subdomain_enum.run(logger)
        portscan.run_deep(logger)
        tech_detect.run(logger)
        dir_enum.run(logger)

    elif mode == "3":
        subdomain_enum.run_stealth(logger)
        portscan.run_stealth(logger)
        tech_detect.run(logger)

    else:
        logger.error("[!] Invalid scan mode. Please enter 1, 2, or 3.")
        sys.exit(1)

    logger.info("[✓] Recon complete.")

if __name__ == "__main__":
    main()
