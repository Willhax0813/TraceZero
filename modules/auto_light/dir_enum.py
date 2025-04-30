# modules/auto_light/dir_enum.py

import subprocess
import os

def run(live_file, output_dir):
    wordlist = "wordlists/common.txt"
    dir_enum_dir = os.path.join(output_dir, "directories")
    os.makedirs(dir_enum_dir, exist_ok=True)

    print("  [-] Running Dirsearch on live domains...")
    try:
        with open(live_file, "r") as f:
            targets = [line.strip().split()[0] for line in f if line.strip()]

        for url in targets:
            safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_")
            out_file = os.path.join(dir_enum_dir, f"{safe_name}.txt")

            subprocess.run([
                "python3", "tools/dirsearch/dirsearch.py",
                "-u", url,
                "-e", "php,html,js",
                "-w", wordlist,
                "--plain-text-report", out_file
            ], stderr=subprocess.DEVNULL)

        print(f"  [✓] Directory scan completed for {len(targets)} targets.")

    except Exception as e:
        print(f"  [x] Dirsearch scan failed: {e}")
