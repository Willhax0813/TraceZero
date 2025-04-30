# modules/auto_light/auto_light_scan.py

import os
from modules.auto_light import subdomain_enum, httpx_scan, tech_detect, dir_enum
from report import html_report


def main_target(domain, logger):
    output_dir = os.path.join("output", domain)
    os.makedirs(output_dir, exist_ok=True)

    logger.info("[+] Step 1: Subdomain Enumeration...")
    subdomains_file = subdomain_enum.run(domain, output_dir)

    logger.info("[+] Step 2: Checking Live Hosts with HTTPX...")
    live_file = httpx_scan.run(subdomains_file, output_dir)

    logger.info("[+] Step 3: Detecting Web Technologies...")
    tech_detect.run(live_file, output_dir)

    logger.info("[+] Step 4: Directory Bruteforce...")
    dir_enum.run(live_file, output_dir)

    logger.info("[✓] Step 5: Auto HTML Report...")
    html_report.generate(output_dir)


# Optional legacy main runner
if __name__ == "__main__":
    print("[!] This module is intended to be imported from main.py")
