# banner.py
from rich.console import Console
from rich.text import Text

console = Console()

# banner/banner.py

try:
    from rich.console import Console
    from rich.text import Text
    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


def banner_tracezero_ascii():
    ascii_banner = r"""
 _________  ___  _________  ____  _______  ____ 
/_  __/ _ \/ _ |/ ___/ __/ /_  / / __/ _ \/ __ \
 / / / , _/ __ / /__/ _/    / /_/ _// , _/ /_/ /
/_/ /_/|_/_/ |_|\___/___/   /___/___/_/|_|\____/ 
                                               
"""
    if RICH_AVAILABLE:
        console.print(Text(ascii_banner, style="bold italic blue"))
        console.print("[green]Infiltrate. Extract. Vanish.[/green]\n")
    else:
        print(ascii_banner)
        print("Infiltrate. Extract. Vanish.\n")

