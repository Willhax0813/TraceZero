# 🦊 TraceZero

**Infiltrate. Extract. Vanish.**

TraceZero is a modular and automated recon tool focused on stealthy, rapid, and clean reconnaissance. Ideal for bug bounty hunters, pentesters, and red teamers.

---

## ⚡ Features (Auto Light Scan)

- ✅ Subdomain Enumeration (`assetfinder`, `subfinder`)
- ✅ Live Subdomain Detection (`httpx`)
- ✅ Web Technology Fingerprinting (`whatweb`)
- ✅ Directory Bruteforce (`dirsearch`)
- ✅ Clean & Structured HTML Report (auto-generated)
- ✅ Auto opens result in browser after scan

---

## 📷 Preview Screenshot

### 🔍 Full HTML Report (auto_light_scan result)
![Auto Light Report Preview](screenshots/report_preview.png)

> You can generate this with:
```bash
python main.py
```

---

## 📁 Output Structure
```
output/
└── targetdomain.com/
    ├── subdomains.txt
    ├── live_subdomains.txt
    ├── tech_detect.txt
    ├── directories/
    │   └── dirsearch_<target>.txt
    └── report.html
```

---

## 🛠 Requirements

Make sure these tools are installed (auto installer included):
- `assetfinder`
- `subfinder`
- `httpx`
- `whatweb`
- `dirsearch`

---

## 🚀 Run the Tool
```bash
python main.py
```
Follow prompts to enter target and select scan mode.

---

## 💡 Roadmap (Planned Features)
- [ ] Highlight HTTP status (200/403/etc)
- [ ] Export report to PDF
- [ ] Screenshot support via gowitness
- [ ] Risk tagging (admin/dev/login/etc)
- [ ] Custom rate limit & wordlist support

---

## 🤝 Contribute
PRs welcome! Modular by design, easily expandable.

---

## 📜 License
MIT License
