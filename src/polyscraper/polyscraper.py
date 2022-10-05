import time

from bs4 import BeautifulSoup

from .helpers import color, colortime, config, headers
from .scrape import check, scrapeData
from .webhook import dataError, notify


def run(link, scrape):
        
    data = scrapeData(check(url=link, headers=headers))
    
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
            print(f"{colortime()}[{color(style='green', text='INSTOCK')}] {scrape[1]}")
            return
        else:
            time.ctime()
            print(f"{colortime()}[{color(style='fail', text='OUT OF STOCK')}] {scrape[1]}")
