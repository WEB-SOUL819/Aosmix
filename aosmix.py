#!/data/data/com.termux/files/usr/bin/python
import os, psutil, platform, json, time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

# Load themes
themes = {
    "dark_neon": {
        "banner": "cyan",
        "panel_border": "magenta",
        "text": "green"
    },
    "cyberpunk": {
        "banner": "magenta",
        "panel_border": "cyan",
        "text": "bright_green"
    }
}

theme = themes["dark_neon"]

# Clear terminal
os.system("clear")

# Load banner
with open("banner.txt") as f:
    banner = f.read()
console.print(Panel(banner, style=theme["banner"], box=box.DOUBLE, expand=False))

# System Info
def system_info():
    table = Table(title="[bold cyan]System Info", box=box.ROUNDED, border_style=theme["panel_border"])
    table.add_column("Metric", style="magenta")
    table.add_column("Value", style=theme["text"])

    table.add_row("OS", platform.system())
    table.add_row("Release", platform.release())
    table.add_row("CPU Usage", f"{psutil.cpu_percent()}%")
    table.add_row("RAM Usage", f"{psutil.virtual_memory().percent}%")
    table.add_row("Disk Usage", f"{psutil.disk_usage('/').percent}%")

    # Battery
    try:
        batt = psutil.sensors_battery()
        if batt:
            table.add_row("Battery", f"{batt.percent}%")
    except:
        pass

    return table

console.print(system_info())

# Clock & Uptime
now = datetime.now()
clock = now.strftime("%H:%M:%S")
date = now.strftime("%d-%m-%Y")
uptime = time.time() - psutil.boot_time()
up_h = int(uptime // 3600)
up_m = int((uptime % 3600) // 60)

console.print(Panel(f"[cyan]Time: [green]{clock}   Date: [green]{date}\n[cyan]Uptime: [green]{up_h}h {up_m}m", border_style=theme["panel_border"]))

# Futuristic prompt
console.print(f"[bold {theme['text']}]> [bold cyan][AOSMIX:~]$[/bold cyan] ", end="")
