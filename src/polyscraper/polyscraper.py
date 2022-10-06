import time

from .helpers import color, colortime
from .webhook import notify


def run(data):
    if data[2] is True:
        notify(data)
        time.ctime()
        print(f"{colortime()}[{color(style='green', text='INSTOCK')}] {data[1]}")

    elif data[2] is False:
        time.ctime()
        print(f"{colortime()}[{color(style='fail', text='OUT OF STOCK')}] {data[1]}")
    return data
