import time

from bs4 import BeautifulSoup

from .helpers import color, colortime, config, headers
from .scrape import check
from .webhook import dataError, notify


def run(link, scrape):
        
    data = check(
        url=link,
        headers=headers,
    )
    
    if data.status_code != 200: # site response error handling
    
        if config["settings"]["webhooks"] == True:
            dataError(data)
        
        print(data.status_code)
        exit()

    elif data.status_code == 200:

        x = BeautifulSoup(data.content, "html.parser")

        status = x.find(attrs={"aria-label": "Sold out"})

        if status is None:
            notify()
            time.ctime()
            print(f"{colortime()}{scrape[1]} -- {color(style='green', text='INSTOCK')}")
            return
        else:
            time.ctime()
            print(f"{colortime()}{scrape[1]} -- {color(style='fail', text='OUT OF STOCK')}")
