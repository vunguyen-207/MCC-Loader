import json
import os
import webbrowser
from typing import List, Dict, Any

try:
    import requests
except Exception:
    requests = None

try:
    from pystyle import Colors, Write
except Exception:
    Colors = None
    Write = None


SS_TOOLS_URL = "https://raw.githubusercontent.com/vunguyen-207/MCC_Loader/refs/heads/main/sstool"  # optional remote


def cls_csl():
    os.system('cls')


BANNER = """\033[1;39m

                         ░██████╗░██████╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
                         ██╔════╝██╔════╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
                         ╚█████╗░╚█████╗░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
                         ░╚═══██╗░╚═══██╗╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
                         ██████╔╝██████╔╝░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
                         ╚═════╝░╚═════╝░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
\033[1;39m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
       \033[1;39m┌─────────────────────────────────────────── Archive ────────────────────────────────────────────┐            
       \033[1;32m║                           \033[1;39m  Version          : \033[1;32m 1.1.0                                          \033[1;32m║
       \033[1;32m║                           \033[1;39m  Discord          : \033[0m discord.gg/chiterl                             \033[1;32m║         
       \033[1;32m║                           \033[1;39m  Youtube          : \033[1;31m That Vape User ☊                               \033[1;32m║
       \033[1;32m║                           \033[1;39m  Status           : \033[1;32m Free                                           \033[1;32m║
       \033[1;39m└────────────────────────────────────────────────────────────────────────────────────────────────┘
   \033[0;31m                               Create a ticket if u found a client that not working.
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

                                                \033[1;39m┌────────────────────┐         
                                                \033[1;32m║   \033[1;39m   SS-Tools      \033[1;32m║          
                                                \033[1;39m└────────────────────┘
"""


def inputcsl() -> str:
    if Write is not None and Colors is not None:
        try:
            return Write.Input("             [×] >>  ", Colors.red_to_purple, interval=0.0025)
        except Exception:
            pass
    return input(">> ")


def loadss() -> List[Dict[str, Any]]:
    tools: List[Dict[str, Any]] = []
    if SS_TOOLS_URL and requests is not None:
        try:
            r = requests.get(SS_TOOLS_URL, timeout=10)
            if r.ok:
                data = r.json()
                if isinstance(data, list):
                    tools = data
        except Exception:
            pass
    if not tools and os.path.isfile('ss_tools.json'):
        try:
            with open('ss_tools.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    tools = data
        except Exception:
            pass
    return tools


def groupthem(items: List[Dict[str, Any]]):
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for it in items:
        cat = str(it.get('category', 'Uncategorized') or 'Uncategorized')
        grouped.setdefault(cat, []).append(it)
    return grouped


def rq_link(url: str):
    try:
        if not isinstance(url, str) or not url.strip():
            return
        webbrowser.open_new(url.strip())
    except Exception:
        pass


def paginate(items: List[Dict[str, Any]], page_size: int, page_index: int) -> List[Dict[str, Any]]:
    start = page_index * page_size
    end = start + page_size
    return items[start:end]


def browse_list(items: List[Dict[str, Any]], title: str):
    if not items:
        cls_csl()
        print(BANNER)
        print("No items found. Press ENTER to go back.")
        input()
        return

    page = 0
    page_size = 20
    while True:
        cls_csl()
        print(BANNER)
        page_items = paginate(items, page_size, page)
        total_pages = (len(items) - 1) // page_size + 1

        for idx, it in enumerate(page_items, start=1):
            name = str(it.get('name', 'Unknown'))
            version = str(it.get('version_info', '') or '')
            category = str(it.get('category', '') or '')
            label = f"{name}"
            if version:
                label += f" | {version}"
            if category:
                label += f" | {category}"
            print(f"[{idx}] {label}")

        print("\n\033[1;31m[\033[1;39mCommands\033[1;31m]\033[1;39m: [N]ext  [P]rev  [B]ack  [-] Exit  [#] Open item")
        print(f"\033[1;39mPage \033[1;31m{page + 1}\033[1;39m/\033[1;31m{max(total_pages, 1)} \033[1;39m| Total: \033[1;31m{len(items)}\033[0m")
        choice = inputcsl().strip()

        if not choice:
            continue
        up = choice.upper()
        if up == '-':
            return
        if up == 'B':
            return
        if up == 'N':
            if (page + 1) * page_size < len(items):
                page += 1
            continue
        if up == 'P':
            if page > 0:
                page -= 1
            continue

        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(page_items):
                url = page_items[idx - 1].get('download_link')
                rq_link(str(url or ''))
            continue


def open_sstul():
    tools = loadss()
    if not tools:
        cls_csl()
        print("SS-Tools")
        print("Dataset not found. Add ss_tools.json or set MCC_SS_TOOLS_URL.")
        input("Press ENTER to return...")
        return

    grouped = groupthem(tools)
    categories = sorted(grouped.keys())

    while True:
        cls_csl()
        print(BANNER)
        print("[0] All")
        for i, cat in enumerate(categories, start=1):
            count = len(grouped.get(cat, []))
            print(f"[{i}] {cat} ({count})")
        print("\n\033[1;31m[\033[1;39mCommands\033[1;31m]\033[1;39m: [S]earch  [-] Exit  [#] Open category")
        choice = inputcsl().strip()

        if not choice:
            continue
        up = choice.upper()
        if up == '-':
            return
        if up == 'S':
            print("\033[1;39mSearch by name contains:\033[0m")
            query = inputcsl().strip().lower()
            if not query:
                continue
            subset = [t for t in tools if query in str(t.get('name', '')).lower()]
            browse_list(subset, f"Search: {query}")
            continue

        if choice.isdigit():
            idx = int(choice)
            if idx == 0:
                browse_list(tools, "All Tools")
                continue
            if 1 <= idx <= len(categories):
                cat = categories[idx - 1]
                browse_list(grouped.get(cat, []), f"Category: {cat}")
                continue


