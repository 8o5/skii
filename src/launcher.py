import sys
import time


from polyscraper.helpers import cls, colortime, color, config, placeholder
from polyscraper.scrape import scrapeCollections, scrapeProducts
from polyscraper.webhook import startScanning, notify


def startup():
    cls()
    print(f"{color(style='blue', text='STARTED WITH SETTINGS:')} {config['settings']}")
    print("---")

    collections = scrapeCollections(list_collections=[], all_list_collections=[])

    if collections is None:
        raise Exception("Failed scraping collections")

    products = scrapeProducts()

    if products is None:
        raise Exception("Failed scraping products")
        

    for i in config['products']:

        if i is None:
            raise Exception("i is None")

        print(f"{color(style='green', text='SCANNING')} {products.get(i, placeholder).name}") 

        if config["settings"]["webhooks"] == True:

            startScanning(
                product_image=products.get(i, placeholder).img, 
                product_title=products.get(i, placeholder).name, 
                link=i,
                price=products.get(i, placeholder).price, 
                status=products.get(i, placeholder).instock 
            )

    print("---")


startup()


while True:

    products = scrapeProducts()
    
    if products is None:
        raise Exception("Failed scraping products")
    
    print(colortime())

    for i in config['products']:

        if products.get(i, placeholder).instock == "IN STOCK": 
            notify(products=products, current=i)
            print(f"[{color(style='green', text='IN STOCK')}] {products.get(i, placeholder).name}") 

        elif products.get(i, placeholder).instock == "OOS":
            print(f"[{color(style='fail', text='OUT OF STOCK')}] {products.get(i, placeholder).name}") 
    
    print(
        f"Waiting {color(style='blue', text=config['settings']['cooldown'])} seconds"
    )

    time.sleep(config["settings"]["cooldown"])
    