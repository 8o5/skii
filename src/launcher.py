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
                product_image=scrape[0],
                product_title=scrape[1],
                link=config["url"][link],
            )
    print("---")


startup()


while True:

    if link < len(config["url"]):
        run(
            link=config["url"][link],
            scrape=scrapeData(link=config["url"][link]),
        )

        link = link + 1

    else:
        link = 0
        time.sleep(config["settings"]["cooldown"])
        cls()
