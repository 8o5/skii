import time

from utils.__init__ import __sites__, __version__
from polyphia.webhook import notify, startScanning
from utils.helpers import cls, color, colortime, config, findSites, placeholder
from utils.scrape import scrapeData

sites = set()

def clear():
    cls()
    print("  ██████  ██ ▄█▀ ██▓ ██▓\n▒██    ▒  ██▄█▒ ▓██▒▓██▒\n░ ▓██▄   ▓███▄░ ▒██▒▒██▒\n  ▒   ██▒▓██ █▄ ░██░░██░\n▒██████▒▒▒██▒ █▄░██░░██░\n▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒░▓  ░▓  \n░ ░▒  ░ ░░ ░▒ ▒░ ▒ ░ ▒ ░\n░  ░  ░  ░ ░░ ░  ▒ ░ ▒ ░\n      ░  ░  ░    ░   ░  ")
    print(color(style="cyan", text=f"\n{__version__}\n"))

clear()

# [{color(style='purple', text='#')}] TEXT\n
option = input(f"[{color(style='purple', text='1')}] Start Monitoring Products\n[{color(style='purple', text='2')}] Start Monitoring Collections\n[{color(style='purple', text='3')}] Credits\n\n")

clear()

if option == "1":

    print(f"{color(style='blue', text='STARTED MONITORING PRODUCTS WITH SETTINGS:')}")
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

    def initialize(sites):

        products = []
        polyphia_products = None
        babymetal_products = None
        all_collections = []

        for i in sites:

            products = None

            if i == __sites__[0]: # polyphia

                collections = scrapeData(site=i, mode="collections")

                if collections == None:
                    raise Exception("Failed scraping collections")

                all_collections.append(collections[0])

                products = scrapeData(site=i, mode="products")

                if products is None:
                    raise Exception("Failed scraping products")

                polyphia_products = products

                print("here") # debug
                time.sleep(3)


                for value in polyphia_query:

                    print(f"[{color(style='purple', text=i.upper())}] {color(style='green', text='SCANNING')} {products.get(value, placeholder).name}") 

                    if config["settings"]["webhooks"] == True:

                        startScanning(
                            product_image=products.get(value, placeholder).img, 
                            product_title=products.get(value, placeholder).name, 
                            link=value,
                            price=products.get(value, placeholder).price, 
                            status=products.get(value, placeholder).instock, 
                            site=i.capitalize(),
                            site_img=products.get(value, placeholder).site_img, 
                        )
                
        

            elif i == __sites__[1]: # babymetal

                collections = scrapeData(site=i, mode="collections")

                if collections == []:
                    raise Exception("Failed scraping collections")

                all_collections.append(collections)

                products = scrapeData(site=i, mode="products")

                if products is None:
                    raise Exception("Failed scraping products")

                babymetal_products = products

                for value in babymetal_query:

                    print(f"[{color(style='purple', text=i.upper())}] {color(style='green', text='SCANNING')} {products.get(value, placeholder).name}") 


                    if config["settings"]["webhooks"] == True:

                        startScanning(
                            product_image=products.get(value, placeholder).img, 
                            product_title=products.get(value, placeholder).name, 
                            link=value,
                            price=products.get(value, placeholder).price, 
                            status=products.get(value, placeholder).instock, 
                            site=i.capitalize(),
                            site_img=products.get(value, placeholder).site_img, 
                        )
                
            
            else:
                polyphia_products = None
                babymetal_products = None
                raise Exception(f"failed to initialize {i} from {sites}")

        if polyphia_products != None and babymetal_products != None:
            return polyphia_products, babymetal_products

        elif polyphia_products == None and babymetal_products != None:
            return None, babymetal_products

        elif polyphia_products != None and babymetal_products == None:
            return polyphia_products, None

    try:
        if lengths["polyphia"] > 0:
            sites.add("polyphia")
        
        if lengths["babymetal"] > 0:
            sites.add("babymetalstore")
    
    except:
        raise Exception(f"{lengths} are not bigger than 0")

    init = initialize(sites=sites) # sort this

    if init == None:
        raise Exception(f"init == {init}")

    print()

    while True:
        
        print(colortime())

        if lengths["polyphia"] > 0:

            for value in polyphia_query:
                products = init[0]
                if products == None:
                    raise Exception(f"products == {products}")
                if products.get(value, placeholder).instock == "IN STOCK": 
                    notify(products=products, current=value)
                    print(f"[{color(style='purple', text='POLYPHIA')}] [{color(style='green', text='IN STOCK')}] {products.get(value, placeholder).name}") 

                elif products.get(value, placeholder).instock == "OOS":
                    print(f"[{color(style='purple', text='POLYPHIA')}] [{color(style='fail', text='OUT OF STOCK')}] {products.get(value, placeholder).name}") 

        
        if lengths["babymetal"] > 0:
            
            for value in babymetal_query:
                products = init[1]
                if products == None:
                    raise Exception(f"products == {products}")
                if products.get(value, placeholder).instock == "IN STOCK": 
                    # notify(products=products, current=value)
                    print(f"[{color(style='purple', text='BABYMETALSTORE')}] [{color(style='green', text='IN STOCK')}] {products.get(value, placeholder).name}") 

                elif products.get(value, placeholder).instock == "OOS":
                    print(f"[{color(style='purple', text='BABYMETALSTORE')}] [{color(style='fail', text='OUT OF STOCK')}] {products.get(value, placeholder).name}") 
            

        print(
                f"\n[{color(style='cyan', text='SYSTEM')}] Waiting {color(style='blue', text=config['settings']['cooldown'])} seconds\n"
            )

        time.sleep(config["settings"]["cooldown"])

elif option == "2":
    print("yay")

elif option == "3":
    print(f"made by {color(style='purple', text='8o5')} and {color(style='cyan', text='curiositIy')}")

else:
    print(color(style='fail', text='ERROR: INVALID OPTION'))
