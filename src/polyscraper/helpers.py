import os
import time
import discord
import toml

link = 0


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def colortime():
    time.ctime()
    return f"{bcolors.HEADER}[{time.ctime()}] {bcolors.ENDC}"


def color(style, text):
    if style == "fail":
        return f"{bcolors.FAIL}{text}{bcolors.ENDC}"
    if style == "blue":
        return f"{bcolors.OKBLUE}{text}{bcolors.ENDC}"
    if style == "cyan":
        return f"{bcolors.OKCYAN}{text}{bcolors.ENDC}"
    if style == "green":
        return f"{bcolors.OKGREEN}{text}{bcolors.ENDC}"
    if style == "warning":
        return f"{bcolors.WARNING}{text}{bcolors.ENDC}"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}


def cls():
    os.system("cls" if os.name == "nt" else "clear")


config = toml.load("src/config.toml")

match config:
    case {
        "url": list(),
        "settings": {"webhooks": bool()},
        "discord": {"webhook": str(), "my_id": int()},
    }:
        pass
    case _:
        raise ValueError(f"invalid configuration: {config}")

mention = config["discord"]["my_id"]
