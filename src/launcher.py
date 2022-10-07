import sys
import time

from polyscraper import (
    cls,
    color,
    colortime,
    config,
    scrapeCollections,
    scrapeProducts,
    startScanning,
    notify
)

link = 0


def startup():
    cls()
    print(f"{color(style='blue', text='STARTED WITH SETTINGS:')} {config['settings']}")
    print("---")

    collections = scrapeCollections(list_collections=[], all_list_collections=[])

    if collections is None:
        sys.exit("@nic handle your shit better i get so many typing errors")

    products = scrapeProducts()

    if products is None:
        sys.exit("see above message :middle_finger:")

    for i in config['products']:

        if i is None:
            sys.exit("No data found.")

        print(f"{color(style='green', text='SCANNING')} {products.get(i).name}")

        if config["settings"]["webhooks"] == True:

            startScanning(
                product_image=products.get(i).img,
                product_title=products.get(i).name,
                link=i,
                price=products.get(i).price,
                status=products.get(i).instock
            )

    print("---")


startup()


while True:

    products = scrapeProducts()

    for i in config['products']:

        if products.get(i).instock != "OOS":
            notify(products=products, current=i)
            time.ctime()
            print(f"{colortime()}[{color(style='green', text='INSTOCK')}] {products.get(i).name}")

        else:
            time.ctime()
            print(f"{colortime()}[{color(style='fail', text='OOS')}] {products.get(i).name}")
    
    print(
        f"{colortime()}Waiting {color(style='blue', text=config['settings']['cooldown'])} seconds"
    )

    time.sleep(config["settings"]["cooldown"])