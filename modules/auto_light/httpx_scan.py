# modules/auto_light/httpx_scan.py

import subprocess
import os

def run(subdomains_file, output_dir):
    live_out = os.path.join(output_dir, "live_subdomains.txt")
    print("  [-] Running HTTPX to detect live domains...")
    try:
        with open(live_out, "w") as f:
            subprocess.run([
                "httpx", "-silent", "-threads", "50", "-status-code", "-title", "-tech-detect", 
                "-no-color", "-timeout", "5", "-ip", "-follow-redirects", "-retries", "1",
                "-rate-limit", "100", "-l", subdomains_file
            ], stdout=f, stderr=subprocess.DEVNULL)

        with open(live_out, "r") as check:
            lines = check.readlines()
            print(f"  [✓] Found {len(lines)} live targets with HTTP/HTTPS")

        return live_out

    except Exception as e:
        print(f"  [x] HTTPX scan failed: {e}")
        return ""
