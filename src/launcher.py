import time

from polyscraper.helpers import cls, colortime, color, config, link
from polyscraper.polyscraper import run
from polyscraper.scrape import scrapeCollection, scrapeData, scrapeStatic
from polyscraper.webhook import dataError, startScanning

data=scrapeData(link=config["url"][link])

def startup(data):

    cls()
    
    collections=[]

    print(f"{color(style='blue', text='STARTED WITH SETTINGS:')} {config['settings']}")

    print("---")
    
    for i in config["url"]:
        
        if data is None:
            exit()
        
        collections.append(scrapeCollection(link=i))
        collections = list(set(collections))
        
        print(f"{color(style='green', text='SCANNING')} {data[1]}") 

        if config["settings"]["webhooks"] == True:

            startScanning(
                product_image=data[0], 
                product_title=data[1], 
                link=i,
            )
    
    
    for i in collections:
        scrapeStatic(collection=i)
    
    
    print("---")


startup(data=data)


while True:

    if link < len(config["url"]):
        run(
            data=data,
        )

        link = link + 1
        
        print(f"{colortime()}Waiting {color(style='blue', text=config['settings']['cooldown'])} seconds")
        
        time.sleep(config["settings"]["cooldown"])
        data = scrapeData(link=config["url"][link])

    else:
        link = 0
        time.sleep(config["settings"]["cooldown"])