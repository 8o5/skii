import time

from polyscraper.helpers import cls, colortime, color, config, link
from polyscraper.polyscraper import run
from polyscraper.scrape import scrapeData
from polyscraper.webhook import startScanning

def startup():
    
    cls()
    
    print(f"{color(style='blue', text='STARTED WITH SETTINGS:')} {config['settings']}")
    
    print("---")
    for i in config["url"]:
        
        scrape = scrapeData(link=i)
        print(f"{color(style='green', text='SCANNING')} {scrape[1]}")

        if config["settings"]["webhooks"] == True:
            
            startScanning(
                product_image = scrape[0],
                product_title = scrape[1]
                )
    print("---")
    
            
            

startup()

link = 1

while True:
    
    run(
        link=config['url'][link], 
        scrape=scrapeData(link=config["url"][link])
        )
    
    if link == len(config["url"]):
        link = 1
    
    else:
        while link < len(config["url"]):
            
            if link == len(config["url"]):
                link = 1
                break
            
            print(len(config["url"]))
            print(link)
            link = link + 1
            
            run(
                link=config['url'][link], 
                scrape=scrapeData(link=config["url"][link])
                )
        
        
    time.sleep(config["settings"]["cooldown"])
    cls()