import time

from utils.__init__ import __version__, __sites__
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

site = []

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

    for i in site:

        if site[i] == __sites__[0]: # polyphia

            collections = scrapeCollections(list_collections=[], all_list_collections=[]) # collections and products only need to be scraped once per site

            if collections is None:
                raise Exception("Failed scraping collections")

            products = scrapeProducts(site=site)

            if products is None:
                raise Exception("Failed scraping products")

            for value in polyphia_query:
                print(f"[{color(style='purple', text=site.capitalize())}] {color(style='green', text='SCANNING')} {products.get(value, placeholder).name}") 

                if config["settings"]["webhooks"] == True:

                    startScanning(
                        product_image=products.get(value, placeholder).img, 
                        product_title=products.get(value, placeholder).name, 
                        link=value,
                        price=products.get(value, placeholder).price, 
                        status=products.get(value, placeholder).instock, 
                        site=site.capitalize(),
                        site_img=products.get(value, placeholder).site_img, 
                    )
            
            print()
    

        elif site[i] == __sites__[1]: # babymetal
            products = None
            raise Exception(f"failed to initialize {site}")
        
        else:
            products = None
            raise Exception(f"failed to initialize {site}")

        return products

if lengths["polyphia"] > 0:
    site.append("polyphia")
    products = initialize(site=site) # lowercase
else:
    raise Exception

while True:
    
    print(colortime())

    if lengths["polyphia"] > 0:
        for value in polyphia_query:

            if products.get(value, placeholder).instock == "IN STOCK": 
                notify(products=products, current=value)
                print(f"[{color(style='purple', text='Polyphia')}] [{color(style='green', text='IN STOCK')}] {products.get(value, placeholder).name}") 

            elif products.get(value, placeholder).instock == "OOS":
                print(f"[{color(style='purple', text='Polyphia')}] [{color(style='fail', text='OUT OF STOCK')}] {products.get(value, placeholder).name}") 
        
        print(
            f"\n[{color(style='cyan', text='SYSTEM')}] Waiting {color(style='blue', text=config['settings']['cooldown'])} seconds\n"
        )
    


    time.sleep(config["settings"]["cooldown"])
    