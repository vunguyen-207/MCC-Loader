import json
import os
import webbrowser
from typing import List, Dict, Any

try:
    import requests
except Exception:
    requests = None  # Just in case..

try:
    from pystyle import Colors, Write
except Exception:
    Colors = None
    Write = None


mccarchive = "https://raw.githubusercontent.com/vunguyen-207/MCC_Loader/refs/heads/main/mc"


def cls_csl():
    os.system('cls')


BANNER = """

                     ███╗░░░███╗██╗███╗░░██╗███████╗░█████╗░██████╗░░█████╗░███████╗████████╗
                     ████╗░████║██║████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
                     ██╔████╔██║██║██╔██╗██║█████╗░░██║░░╚═╝██████╔╝███████║█████╗░░░░░██║░░░
                     ██║╚██╔╝██║██║██║╚████║██╔══╝░░██║░░██╗██╔══██╗██╔══██║██╔══╝░░░░░██║░░░
                     ██║░╚═╝░██║██║██║░╚███║███████╗╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░
                     ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░
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
                                                \033[1;32m║   \033[1;39m   Minecraft     \033[1;32m║          
                                                \033[1;39m└────────────────────┘
                                                
"""


def inputcsl() -> str:
    if Write is not None and Colors is not None:
        try:
            return Write.Input("             [×] >>  ", Colors.red_to_purple, interval=0.0025)
        except Exception:
            pass
    return input(">> ")


def analyse_clients() -> List[Dict[str, Any]]:
    clients: List[Dict[str, Any]] = []

    if requests is not None:
        try:
            resp = requests.get(mccarchive, timeout=10)
            if resp.ok:
                data = resp.json()
                if isinstance(data, list):
                    clients = data
        except Exception:
            pass

    # A little fallback, maybe try it lol
    if not clients and os.path.isfile('minecraft_clients.json'):
        try:
            with open('minecraft_clients.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    clients = data
        except Exception:
            pass

    return clients


def groupthem(clients: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for item in clients:
        category = str(item.get('category', 'Uncategorized') or 'Uncategorized')
        grouped.setdefault(category, []).append(item)
    return grouped


def printt():
    print(BANNER)


def paginate(items: List[Dict[str, Any]], page_size: int, page_index: int) -> List[Dict[str, Any]]:
    start = page_index * page_size
    end = start + page_size
    return items[start:end]


def rq_link(url: str):
    try:
        if not isinstance(url, str) or not url.strip():
            return
        webbrowser.open_new(url.strip())
    except Exception:
        pass


def browse_list(items: List[Dict[str, Any]], title: str):
    if not items:
        cls_csl()
        printt()
        print("No clients found. Press ENTER to go back.")
        input()
        return

    page = 0
    page_size = 20
    while True:
        cls_csl()
        printt()
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

def openclient():
    clients = analyse_clients()
    if not clients:
        cls_csl()
        printt()
        print("Unable to load dataset. Ensure internet connection.")
        input("Press ENTER to return...")
        return

    grouped = groupthem(clients)
    categories = sorted(grouped.keys())

    while True:
        cls_csl()
        printt()
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
            subset = [c for c in clients if query in str(c.get('name', '')).lower()]
            browse_list(subset, f"Search: {query}")
            continue

        if choice.isdigit():
            idx = int(choice)
            if idx == 0:
                browse_list(clients, "All Clients")
                continue
            if 1 <= idx <= len(categories):
                cat = categories[idx - 1]
                browse_list(grouped.get(cat, []), f"Category: {cat}")
                continue


