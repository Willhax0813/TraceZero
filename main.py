from banner import banner_tracezero_ascii
from rich.console import Console
from utils.dependency_check import check_and_install_dependencies
from config.settings import SCAN_MODE
from scanner import subdomain_enum, portscan, tech_detect, dir_enum
from report.logger import init_logger

import sys

console= Console()


def main():
    # Tampilkan banner
    banner_tracezero_ascii()

    # Inisialisasi logger
    logger = init_logger()
    logger.info(f"[+] Starting TRACEZERO in {SCAN_MODE.upper()} mode")

    # Auto check & install dependency
    check_and_install_dependencies(logger)

    # Eksekusi tools berdasarkan mode
    if SCAN_MODE == "light":
        subdomain_enum.run(logger)
        portscan.run_light(logger)
        tech_detect.run(logger)
        dir_enum.run(logger)

    elif SCAN_MODE == "deep":
        subdomain_enum.run(logger)
        portscan.run_deep(logger)
        tech_detect.run(logger)
        dir_enum.run(logger)
        # Tambahkan modul lain seperti vuln scan, JS parser, takeover, dll

    elif SCAN_MODE == "stealth":
        subdomain_enum.run_stealth(logger)
        portscan.run_stealth(logger)
        tech_detect.run(logger)

    else:
        logger.error("[!] Invalid scan mode. Please check settings.py")
        sys.exit(1)

    logger.info("[+] Recon complete.")


if __name__ == "__main__":
    main()
