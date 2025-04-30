# report/html_report.py

import os
from datetime import datetime

def generate(output_dir):
    sub_file = os.path.join(output_dir, "subdomains.txt")
    live_file = os.path.join(output_dir, "live_subdomains.txt")
    tech_file = os.path.join(output_dir, "tech_detect.txt")
    dir_path = os.path.join(output_dir, "directories")
    report_file = os.path.join(output_dir, "report.html")

    try:
        with open(report_file, "w") as f:
            f.write("<html><head><title>TraceZero Auto Light Report</title></head><body>")
            f.write(f"<h1>TraceZero Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</h1>")

            f.write("<h2>Live Subdomains</h2><ul>")
            with open(live_file, "r") as live:
                for line in live:
                    url = line.strip().split()[0]
                    f.write(f"<li><a href='{url}' target='_blank'>{url}</a></li>")
            f.write("</ul>")

            f.write("<h2>Technology Fingerprints</h2><pre>")
            with open(tech_file, "r") as tech:
                f.write(tech.read())
            f.write("</pre>")

            f.write("<h2>Directory Bruteforce</h2>")
            for filename in os.listdir(dir_path):
                path = os.path.join(dir_path, filename)
                if os.path.isfile(path):
                    f.write(f"<h3>{filename.replace('.txt', '')}</h3><pre>")
                    with open(path, "r") as d:
                        f.write(d.read())
                    f.write("</pre>")

            f.write("</body></html>")

        print(f"  [✓] HTML report generated: {report_file}")
    except Exception as e:
        print(f"  [x] Failed to generate HTML report: {e}")
