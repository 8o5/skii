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


sites = findSites() # make it import the needed modules depending on what sites there are in the set

def startup(site):

    collections = scrapeCollections(list_collections=[], all_list_collections=[]) # collections and products only need to be scraped once per site

    if collections is None:
        raise Exception("Failed scraping collections")

    products = scrapeProducts(site=site)

    if products is None:
        raise Exception("Failed scraping products")
       

    for i in config['products']: # make this loop for all keys that match "site" 

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
                site_img="site_img" # placeholder
            )

    print()

for i in sites:

    if i is None:
            raise Exception("i is None")

    startup(site=i) # loop once for each seperate key in sites dict, ie: polyphia, babymetal


while True:

    products = scrapeProducts(site="") # match line 37 ig
    
    if products is None:
        raise Exception("Failed scraping products")
    
    print(colortime())

    for i in config['products']: # this needs to sync with startup

        if products.get(i, placeholder).instock == "IN STOCK": 
            notify(products=products, current=i)
            print(f"[{color(style='green', text='IN STOCK')}] {products.get(i, placeholder).name}") 

        elif products.get(i, placeholder).instock == "OOS":
            print(f"[{color(style='fail', text='OUT OF STOCK')}] {products.get(i, placeholder).name}") 
    
    print(
        f"\n[{color(style='cyan', text='SYSTEM')}] Waiting {color(style='blue', text=config['settings']['cooldown'])} seconds\n"
    )

    time.sleep(config["settings"]["cooldown"])
    