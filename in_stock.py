import time

import discord
import requests
import toml
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

config = toml.load("config.toml")

match config:
    case {
        "url": {"url": str()},
        "settings": {"webhooks": bool()},
        "discord": {"webhook": str(), "my_id": int()},
    }:
        pass
    case _:
        raise ValueError(f"invalid configuration: {config}")

if config["settings"]["webhooks"] == True:
    webhook = discord.SyncWebhook.from_url(config["discord"]["webhook"])

mention = config["discord"]["my_id"]

def scrapeData():
    data = requests.get(
            url=config["url"]["url"],
            headers=headers,
            timeout=5,
        )
    z = BeautifulSoup(data.content, "html.parser")
    img_location = z.findAll('img', class_="product-featured-media")
    title_location = z.findAll('h1', class_="product-single__title")
    product_image = f"https:{img_location[1]['src']}" # type: ignore
    product_title = title_location[0].text
    return (product_image, product_title)

scrape = scrapeData()

def notify():
    
    if config["settings"]["webhooks"] == True:

        embed = discord.Embed(
            title=f"🎉 ITEM INSTOCK", color=0xCFC00, timestamp=discord.utils.utcnow(), description=scrape[1]
        )

        embed.set_author(
            name=f"Polyphia",
            url="https://www.polyphia.com/",
            icon_url="https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615",
        )  # set author

        embed.set_image(url="")  # set image

        embed.set_thumbnail(
            url=scrape[0]
        )  # set thumbnail

        embed.set_footer(
            text="nic#0002",
            icon_url="https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png",
        )  # set footer

        embed.add_field(name="URL", value=config['url']['url'], inline=False)

        webhook.send(content=f"<@{config['discord']['my_id']}>", embed=embed)


def check(url, headers):

    data = requests.get(
        url,
        headers,
        timeout=5,
    )

    data.raise_for_status()

    if data.status_code != 200:
        
        if config["settings"]["webhooks"] == True:
            embed = discord.Embed(
                title=f"❌ ERROR {data.status_code}",
                description=f'<@{config["my_id"]}>',
                color=0xEE4B2B,
                timestamp=discord.utils.utcnow(),
            )

            embed.set_author(
                name=f"Polyphia",
                url="https://www.polyphia.com/",
                icon_url="https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615",
            )  # set author

            embed.set_image(url="")  # set image

            embed.set_thumbnail(url="")  # set thumbnail

            embed.set_footer(
                text="nic#0002",
                icon_url="https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png",
            )  # set footer

            embed.add_field(name="URL", value=f"{config['url']}s", inline=False)

            webhook.send(content=f"<@{config['my_id']}>", embed=embed)

        print(data.status_code)
        exit()

    elif data.status_code == 200:

        x = BeautifulSoup(data.content, "html.parser")

        status = x.find(attrs={"aria-label": "Sold out"})

        if status is None:
            notify()
            time.ctime()
            print(f"[{time.ctime()}] -- INSTOCK")
            return
        else:
            time.ctime()
            print(f"[{time.ctime()}] -- OOS")


def initialize():
    
    print(f"SCANNING {config['url']['url']}")
    
    if config["settings"]["webhooks"] == True:
        product_image = scrape[0]
        product_title = scrape[1]
        embed = discord.Embed(
            title=f"🔎 STARTED SCANNING", color=0x161955, timestamp=discord.utils.utcnow(), description=product_title
        )

        embed.set_author(
            name="Polyphia",
            url="https://www.polyphia.com/",
            icon_url="https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615",
        )  # set author

        embed.set_image(url="")  # set image

        embed.set_thumbnail(
            url=product_image
        )  # set thumbnail

        embed.set_footer(
            text="nic#0002",
            icon_url="https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png",
        )  # set footer

        embed.add_field(name="URL", value=config["url"]["url"], inline=False)

        webhook.send(
            content=f"<@{mention}>", 
            embed=embed)

    while True:
        check(
            url=config["url"]["url"],
            headers=headers,
        )
        time.sleep(60)

initialize()