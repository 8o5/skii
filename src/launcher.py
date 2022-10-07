import time
<<<<<<< Updated upstream
from typing_extensions import reveal_type

from polyscraper import (
    cls,
    colortime,
    color,
    config,
<<<<<<< Updated upstream
    link,
    run,
    scrapeData,
    scrapeCollection,
=======
    scrapeCollections,
    scrapeProducts,
>>>>>>> Stashed changes
    startScanning,
    notify
)
=======

from polyscraper.helpers import cls, colortime, color, config, link
from polyscraper.polyscraper import run
from polyscraper.scrape import scrapeData, scrapeCollections
from polyscraper.webhook import startScanning
>>>>>>> Stashed changes

data = scrapeData(link=config["url"][link])


def startup(data):

<<<<<<< Updated upstream
    cls()
    
    print(f"{color(style='blue', text='STARTED WITH SETTINGS:')} {config['settings']}")

    print("---")
    
    collections = scrapeCollections()

    for i in collections:

        if data is None:
            exit()

<<<<<<< Updated upstream
        collections.append(scrapeData(link=i))
        print(collections)  # debug

=======
>>>>>>> Stashed changes
        print(f"{color(style='green', text='SCANNING')} {data[1]}")
=======
    for i in config['products']:

        if i is None:
            sys.exit("No data found.")

        print(f"{color(style='green', text='SCANNING')} {products.get(i).name}")
>>>>>>> Stashed changes

        if config["settings"]["webhooks"] == True:

            startScanning(
                product_image=products.get(i).img,
                product_title=products.get(i).name,
                link=i,
                price=products.get(i).price,
                status=products.get(i).instock
            )

    print("---")


<<<<<<< Updated upstream
startup(data=data)


while True:
    link = 0 
    if link < len(config["url"]):
        run(
            data=data,
        )
=======
startup()


while True:
>>>>>>> Stashed changes

    products = scrapeProducts()

    for i in config['products']:

        if products.get(i).instock != "OOS":
            notify(products=products, current=i)
            time.ctime()
            print(f"{colortime()}[{color(style='green', text='INSTOCK')}] {products.get(i).name}")

<<<<<<< Updated upstream
        time.sleep(config["settings"]["cooldown"])
        data = scrapeData(link=config["url"][link])
=======
        else:
            time.ctime()
            print(f"{colortime()}[{color(style='fail', text='OOS')}] {products.get(i).name}")
    
    print(
        f"{colortime()}Waiting {color(style='blue', text=config['settings']['cooldown'])} seconds"
    )
>>>>>>> Stashed changes

    time.sleep(config["settings"]["cooldown"])
