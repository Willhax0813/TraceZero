# config/settings_local.py
# Override paths/tools/settings here for your local machine (not pushed to GitHub)

import os

from config.settings import TOOL_PATHS

TOOL_PATHS["subfinder"] = os.path.expanduser("~/go/bin/subfinder")
TOOL_PATHS["assetfinder"] = os.path.expanduser("~/go/bin/assetfinder")
TOOL_PATHS["rustscan"] = os.path.expanduser("~/.cargo/bin/rustscan")
TOOL_PATHS["dirsearch"] = os.path.join("tools", "dirsearch", "dirsearch.py")
