import discord

from .helpers import config, link, mention
from .scrape import scrape

if config["settings"]["webhooks"] == True:
    webhook = discord.SyncWebhook.from_url(config["discord"]["webhook"])


def startScanning(product_image, product_title, link):
    embed = discord.Embed(
        title=f"🔎 STARTED SCANNING",
        color=0x161955,
        timestamp=discord.utils.utcnow(),
        description=product_title,
    )

    embed.set_author(
        name="Polyphia",
        url="https://www.polyphia.com/",
        icon_url="https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615",
    )  # set author

    embed.set_image(url="")  # set image

    embed.set_thumbnail(url=product_image)  # set thumbnail

    embed.set_footer(
        text="nic#0002",
        icon_url="https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png",
    )  # set footer

    embed.add_field(name="URL", value=link, inline=False)

    webhook.send(content="", embed=embed)


def notify():

    if config["settings"]["webhooks"] == True:

        embed = discord.Embed(
            title=f"🎉 ITEM INSTOCK",
            color=0xCFC00,
            timestamp=discord.utils.utcnow(),
            description=scrape[1],
        )

        embed.set_author(
            name=f"Polyphia",
            url="https://www.polyphia.com/",
            icon_url="https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615",
        )  # set author

        embed.set_image(url="")  # set image

        embed.set_thumbnail(url=scrape[0])  # set thumbnail

        embed.set_footer(
            text="nic#0002",
            icon_url="https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png",
        )  # set footer

        embed.add_field(name="URL", value=config["url"]["url"], inline=False)

        webhook.send(content=f"<@{config['discord']['my_id']}>", embed=embed)


def dataError(data):
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
