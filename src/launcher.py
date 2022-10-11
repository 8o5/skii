import time

from polyphia.__init__ import __version__, __sites__
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

info = findSites()

poly = info[0]
babymetal = info[1]
polyphia_query = info[2]
babymetal_query = info[3]

lengths = (
    {
    "polyphia": poly,
    "babymetal": babymetal,
        }
    )

def initialize(site):

    if site == __sites__[0]:

        collections = scrapeCollections(list_collections=[], all_list_collections=[]) # collections and products only need to be scraped once per site

        if collections is None:
            raise Exception("Failed scraping collections")

        products = scrapeProducts(site=site)

        if products is None:
            raise Exception("Failed scraping products")

        for i in range(lengths['polyphia']):
            if i is None:
                raise Exception("i is None") 
            
            for value in polyphia_query:
                print(f"[{color(style='purple', text=site.upper(0))}] {color(style='green', text='SCANNING')} {products.get(value, placeholder).name}") 

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
        
        

            

    elif site == "babymetal":
        products = None
        raise Exception(f"failed to initialize {site}")
    
    else:
        products = None
        raise Exception(f"failed to initialize {site}")

    return products

if lengths["polyphia"] > 0:
    products = initialize(site="polyphia")
else:
    raise Exception

while True:
    
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
    