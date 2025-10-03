# MCC-Loader

MCC-Loader is a command-line tool that helps you browse a large community archive of **Minecraft clients**, search them by name, explore by **category**, and open their download links directly in your default web browser. The client list is fetched dynamically from a JSON endpoint, with a local JSON fallback for offline usage.

> ⚙️ Status: **Free** · Version: **1.1.0**

---

## ✨ Features

- **Browse all clients** or by **category** (with item counts).
- **Search** clients by name (substring match).
- **Pagination** support (default 20 items per page).
- **Open download links** directly in your browser.
- **Offline fallback**: if the API fails, the app can load from a local `minecraft_clients.json` file.

> Note: Designed primarily for **Windows Terminal / CMD / PowerShell** (uses `cls` and `msvcrt`).

---

## 🧩 Project Structure

```

consmath/
├─ minecraftt.py   # core UI/logic: banner, menu, pagination, browsing & open links
├─ credits.py      # credits screen (ASCII art & community list)
├─ sstul.py        # helper utilities (UI, input fallbacks, etc.)
└─ **init**.py
main.py              # entrypoint, menu navigation

````

- **Data source**: JSON endpoint with client metadata (name, download_link, category, version_info).
- **CLI interface**: styled with `pystyle` (fallbacks to standard `input()` if not installed).
- **Open download links**: uses `webbrowser.open_new()`.

---

## 🚀 Installation

### Requirements
- **Python 3.8+**
- **Windows** OS (recommended)  
  > Linux/macOS may need minor adjustments (`cls` → `clear`, remove `msvcrt`).

### Install dependencies

Currently no `requirements.txt` included. Install manually:

```bash
pip install requests pystyle colorama
````

> If you don’t care about fancy colors, you can skip `pystyle`. The program will fallback gracefully.

---

## ▶️ Usage

```bash
python main.py
```

### Key Controls

* `N` — next page
* `P` — previous page
* `S` — search (in category view)
* `B` — back
* `-` — exit
* Enter **item number** to open the client’s download link

---

## 🌐 Data Source

* Primary: JSON endpoint (online)
* Fallback: `minecraft_clients.json` (must be in the same folder)

If the API is unavailable, MCC-Loader will automatically attempt the local file.

---

## 🧪 Quick Demo

1. Run `python main.py`
2. Choose `[0] All` to list all clients
3. Use `N`/`P` to paginate
4. Enter a number to open the download link

---

## 🛠️ Development

### Client data format

Each record looks like:

```json
{
  "name": "Example Client",
  "download_link": "https://example.com/download",
  "category": "Ghost",
  "version_info": "1.8.9"
}
```

---

## 🙏 Credits

* ASCII art & community credits: see [`consmath/credits.py`](consmath/credits.py)
* CLI colors & styling: [`pystyle`](https://pypi.org/project/pystyle/), [`colorama`](https://pypi.org/project/colorama/)

---

## ⚖️ Disclaimer

MCC-Loader only **lists** download links provided by third parties.
Please ensure that downloading/using these clients complies with **Mojang/Microsoft’s terms of service** and the rules of any server you join. The author is **not responsible** for misuse.
