import time
<<<<<<< Updated upstream
from typing_extensions import reveal_type

from polyscraper import (
    cls,
    colortime,
    color,
    config,
    link,
    run,
    scrapeData,
    scrapeCollection,
    startScanning,
)
=======

from polyscraper.helpers import cls, colortime, color, config, link
from polyscraper.polyscraper import run
from polyscraper.scrape import scrapeData, scrapeCollections
from polyscraper.webhook import startScanning
>>>>>>> Stashed changes

data = scrapeData(link=config["url"][link])


def startup(data):

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

        if config["settings"]["webhooks"] == True:

            startScanning(
                product_image=data[0],
                product_title=data[1],
                link=i,
            )

    print("---")


startup(data=data)


while True:
    link = 0  # @nic you should actually define it first so you don't get possibly unbound error
    if link < len(config["url"]):
        run(
            data=data,
        )

        # link = link + 1
        link += 1
        # @nic we can actually use this method of adding numbers instead

        print(
            f"{colortime()}Waiting {color(style='blue', text=config['settings']['cooldown'])} seconds"
        )

        time.sleep(config["settings"]["cooldown"])
        data = scrapeData(link=config["url"][link])

    else:
        link = 0
        time.sleep(config["settings"]["cooldown"])
