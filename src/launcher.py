import time

from polyphia.__init__ import __version__
from utils.helpers import cls, color, colortime, config, placeholder, findSites
from polyphia.scrape import scrapeCollections, scrapeProducts
from polyphia.webhook import notify, startScanning


cls()
print("  ██████  ██ ▄█▀ ██▓ ██▓\n▒██    ▒  ██▄█▒ ▓██▒▓██▒\n░ ▓██▄   ▓███▄░ ▒██▒▒██▒\n  ▒   ██▒▓██ █▄ ░██░░██░\n▒██████▒▒▒██▒ █▄░██░░██░\n▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒░▓  ░▓  \n░ ░▒  ░ ░░ ░▒ ▒░ ▒ ░ ▒ ░\n░  ░  ░  ░ ░░ ░  ▒ ░ ▒ ░\n      ░  ░  ░    ░   ░  ")
print(color(style="cyan", text=f"\n{__version__}"))

print()

print(f"{color(style='blue', text='STARTED WITH SETTINGS:')}")
for key, value in config['settings'].items():
    print(key, ':', value)

print()


findSites() # make it import the needed modules depending on what sites there are in the set

def startup(site):

    collections = scrapeCollections(list_collections=[], all_list_collections=[])

    if collections is None:
        raise Exception("Failed scraping collections")

    products = scrapeProducts()

    if products is None:
        raise Exception("Failed scraping products")
       

    for i in config['products']:

        if i is None:
            raise Exception("i is None")

        print(f"[{color(style='purple', text=site.upper(0))}] {color(style='green', text='SCANNING')} {products.get(i, placeholder).name}") 

        if config["settings"]["webhooks"] == True:

            startScanning(
                product_image=products.get(i, placeholder).img, 
                product_title=products.get(i, placeholder).name, 
                link=i,
                price=products.get(i, placeholder).price, 
                status=products.get(i, placeholder).instock, 
                site=site.upper(0),
                site_img=site_img
            )

    print()


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
        f"\n[{color(style='cyan', text='SYSTEM')}] Waiting {color(style='blue', text=config['settings']['cooldown'])} seconds\n"
    )

    time.sleep(config["settings"]["cooldown"])
    