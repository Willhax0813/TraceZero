# modules/auto_light/subdomain_enum.py

import subprocess
import os

def run(domain, output_dir):
    subs_path = os.path.join(output_dir, "subdomains.txt")
    asset_out = os.path.join(output_dir, "assetfinder.txt")
    subfinder_out = os.path.join(output_dir, "subfinder.txt")

    print("  [-] Running Assetfinder...")
    with open(asset_out, "w") as f:
        subprocess.run(["assetfinder", "--subs-only", domain], stdout=f, stderr=subprocess.DEVNULL)

    print("  [-] Running Subfinder...")
    with open(subfinder_out, "w") as f:
        subprocess.run(["subfinder", "-d", domain], stdout=f, stderr=subprocess.DEVNULL)

    print("  [-] Merging & deduplicating...")
    seen = set()
    with open(subs_path, "w") as out:
        for file in [asset_out, subfinder_out]:
            with open(file, "r") as f:
                for line in f:
                    clean = line.strip()
                    if clean and clean not in seen:
                        out.write(clean + "\n")
                        seen.add(clean)

    print(f"  [✓] Subdomain enum done. Total: {len(seen)} subdomains")
    return subs_path
