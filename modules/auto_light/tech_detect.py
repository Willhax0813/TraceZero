# modules/auto_light/tech_detect.py

import subprocess
import os

def run(live_file, output_dir):
    tech_out = os.path.join(output_dir, "tech_detect.txt")
    print("  [-] Running WhatWeb to detect technologies...")

    try:
        with open(live_file, "r") as f:
            targets = [line.strip().split()[0] for line in f if line.strip()]

        with open(tech_out, "w") as out:
            for url in targets:
                out.write(f"=== {url} ===\n")
                subprocess.run(["whatweb", url], stdout=out, stderr=subprocess.DEVNULL)

        print(f"  [✓] Technology detection completed for {len(targets)} targets.")
    except Exception as e:
        print(f"  [x] WhatWeb scan failed: {e}")
