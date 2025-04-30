# report/html_report.py

import os
from datetime import datetime
import subprocess
import re

def clean_ansi(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def format_tech_output(raw_line):
    cleaned = clean_ansi(raw_line).strip()
    if not cleaned or cleaned.startswith('==='):
        return None, None
    parts = cleaned.split(" ", 1)
    url = parts[0]
    details = parts[1] if len(parts) > 1 else "-"
    tech_items = [item.strip() for item in re.split(r',\s*(?=[^\]]*(?:\[|$))', details)]
    return url, "<ul>" + "".join(f"<li>{item}</li>" for item in tech_items) + "</ul>"

def generate(output_dir):
    sub_file = os.path.join(output_dir, "subdomains.txt")
    live_file = os.path.join(output_dir, "live_subdomains.txt")
    tech_file = os.path.join(output_dir, "tech_detect.txt")
    dir_path = os.path.join(output_dir, "directories")
    report_file = os.path.join(output_dir, "report.html")

    try:
        with open(report_file, "w") as f:
            f.write("""
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>TraceZero Report</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f4f4; color: #333; padding: 20px; }
    h1, h2, h3 { color: #2c3e50; }
    pre, code { background: #eaeaea; padding: 10px; border-radius: 5px; overflow-x: auto; }
    table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; vertical-align: top; }
    th { background-color: #f0f0f0; }
    ul { list-style: none; padding-left: 20px; }
    li { padding: 2px 0; }
    a { text-decoration: none; color: #2980b9; }
    a:hover { text-decoration: underline; }
    .section { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 0 5px rgba(0,0,0,0.1); }
  </style>
</head>
<body>
  <h1>TraceZero Report</h1>
  <p>Generated: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
""")

            # Live Subdomains Section
            if os.path.isfile(live_file) and os.path.getsize(live_file) > 0:
                f.write("<div class='section'>\n<h2>Live Subdomains</h2>\n<ul>\n")
                with open(live_file, "r") as live:
                    for line in live:
                        url = line.strip().split()[0]
                        f.write(f"<li><a href='{url}' target='_blank'>{url}</a></li>\n")
                f.write("</ul>\n</div>\n")

            # Tech Detection Section (formatted as table + parsed list)
            if os.path.isfile(tech_file) and os.path.getsize(tech_file) > 0:
                f.write("<div class='section'>\n<h2>Technology Fingerprints</h2>\n<table>\n<tr><th>URL</th><th>Technologies</th></tr>\n")
                with open(tech_file, "r") as tech:
                    for line in tech:
                        url, parsed = format_tech_output(line)
                        if url and parsed:
                            f.write(f"<tr><td><a href='{url}' target='_blank'>{url}</a></td><td>{parsed}</td></tr>\n")
                f.write("</table>\n</div>\n")

            # Directory Bruteforce Section
            if os.path.isdir(dir_path):
                dir_files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
                if dir_files:
                    f.write("<div class='section'>\n<h2>Directory Bruteforce</h2>\n")
                    for filename in dir_files:
                        path = os.path.join(dir_path, filename)
                        f.write(f"<h3>{filename.replace('.txt', '')}</h3><pre>")
                        with open(path, "r") as d:
                            f.write(d.read())
                        f.write("</pre>\n")
                    f.write("</div>\n")

            f.write("</body>\n</html>")

        print(f"  [✓] HTML report generated: {report_file}")

        # Open report in browser automatically (Linux only)
        try:
            subprocess.run(["xdg-open", report_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as open_err:
            print(f"  [!] Could not auto-open report: {open_err}")

    except Exception as e:
        print(f"  [x] Failed to generate HTML report: {e}")