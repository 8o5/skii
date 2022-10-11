import os
import time
from typing import Any, Dict

import toml


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
    
class placeholder:
    img = "https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_360x.png"
    name = "Invalid URL in config.toml"
    price = "$0.00 USD"
    instock = "N/A"


class Product:
    def __init__(self, data: Dict[Any, Any]):
        self._data = data  # _ before attr name means its private, we shouldn't be accessing it from outside this class.

    @property
    def name(self) -> str:
        return self._data["name"]

    @property
    def img(self) -> str:
        return self._data["img"]
        
    @property
    def url(self) -> str:
        return self._data["url"]

    @property
    def instock(self) -> bool:
        return self._data["instock"]

    @property
    def price(self) -> str:
        return self._data["price"]

    @property
    def updated(self) -> str:
        return self._data["updated"]


def colortime():
    time.ctime()
    return f"{bcolors.HEADER}[{time.ctime()}] {bcolors.ENDC}"


def color(style, text):

    colors = {
        "fail": f"{bcolors.FAIL}{text}{bcolors.ENDC}",
        "blue": f"{bcolors.OKBLUE}{text}{bcolors.ENDC}",
        "cyan": f"{bcolors.OKCYAN}{text}{bcolors.ENDC}",
        "green": f"{bcolors.OKGREEN}{text}{bcolors.ENDC}",
        "warning": f"{bcolors.WARNING}{text}{bcolors.ENDC}",
    }

    try:
        return colors[style]
    except KeyError:
        raise Exception("Invalid style.")


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}


def cls():
    os.system("cls" if os.name == "nt" else "clear")


config = toml.load("src/config.toml")

match config:
    case {
        "products": list(),
        "settings": {"cooldown": int(), "webhooks": bool()},
        "discord": {"webhook": str(), "my_id": int()},
    }:
        pass
    case _:
        raise ValueError(f"invalid configuration: {config}")

mention = config["discord"]["my_id"]
