# scanner/subdomain_enum.py

import subprocess
import os
from config import settings


def run(logger):
    target = input("[?] Enter target domain: ").strip()
    output_dir = os.path.join(settings.OUTPUT_DIR, target)
    os.makedirs(output_dir, exist_ok=True)
    
    assetfinder_path = settings.TOOL_PATHS.get("assetfinder", "assetfinder")
    subfinder_path = settings.TOOL_PATHS.get("subfinder", "subfinder")

    assetfinder_out = os.path.join(output_dir, "assetfinder.txt")
    subfinder_out = os.path.join(output_dir, "subfinder.txt")
    final_out = os.path.join(output_dir, "subdomains.txt")

    logger.info("[+] Running Assetfinder...")
    with open(assetfinder_out, "w") as f:
        subprocess.run([assetfinder_path, "--subs-only", target], stdout=f, stderr=subprocess.DEVNULL)

    logger.info("[+] Running Subfinder...")
    with open(subfinder_out, "w") as f:
        subprocess.run([subfinder_path, "-d", target], stdout=f, stderr=subprocess.DEVNULL)

    # Merge and deduplicate
    logger.info("[+] Merging results...")
    with open(final_out, "w") as out:
        seen = set()
        for file in [assetfinder_out, subfinder_out]:
            with open(file, "r") as f:
                for line in f:
                    clean = line.strip()
                    if clean and clean not in seen:
                        out.write(clean + "\n")
                        seen.add(clean)

    logger.info(f"[✓] Subdomain enumeration complete. Found {len(seen)} subdomains.")
    logger.info(f"[✓] Saved to: {final_out}")


def run_stealth(logger):
    logger.info("[~] Stealth mode: using only passive tool Assetfinder")
    target = input("[?] Enter target domain: ").strip()
    output_dir = os.path.join(settings.OUTPUT_DIR, target)
    os.makedirs(output_dir, exist_ok=True)

    assetfinder_path = settings.TOOL_PATHS.get("assetfinder", "assetfinder")
    assetfinder_out = os.path.join(output_dir, "assetfinder.txt")
    final_out = os.path.join(output_dir, "subdomains.txt")

    logger.info("[+] Running Assetfinder...")
    with open(assetfinder_out, "w") as f:
        subprocess.run([assetfinder_path, "--subs-only", target], stdout=f, stderr=subprocess.DEVNULL)

    # Dedup only
    with open(final_out, "w") as out:
        seen = set()
        with open(assetfinder_out, "r") as f:
            for line in f:
                clean = line.strip()
                if clean and clean not in seen:
                    out.write(clean + "\n")
                    seen.add(clean)

    logger.info(f"[✓] Stealth subdomain scan complete. Found {len(seen)} subdomains.")
    logger.info(f"[✓] Saved to: {final_out}")
