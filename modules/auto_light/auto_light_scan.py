# modules/auto_light/auto_light_scan.py

import os
from modules.auto_light import subdomain_enum, httpx_scan, tech_detect, dir_enum
from report import html_report


def main():
    print("\n[?] Enter your target domain:")
    domain = input("> ").strip()

    output_dir = os.path.join("output", domain)
    os.makedirs(output_dir, exist_ok=True)

    print("\n[+] Step 1: Subdomain Enumeration...")
    subdomains_file = subdomain_enum.run(domain, output_dir)

    print("\n[+] Step 2: Checking Live Hosts with HTTPX...")
    live_file = httpx_scan.run(subdomains_file, output_dir)

    print("\n[+] Step 3: Detecting Web Technologies...")
    tech_detect.run(live_file, output_dir)

    print("\n[+] Step 4: Directory Bruteforce...")
    dir_enum.run(live_file, output_dir)

    print("\n[+] Step 5: Generating Final Report...")
    html_report.generate(output_dir)

    print("\n[✓] Auto Light Scan completed. Check output folder for results.")


if __name__ == "__main__":
    main()
