import discord
from utils.helpers import color, config
from utils.__init__ import __sites__

if config["settings"]["webhooks"] == True:
    webhook = discord.SyncWebhook.from_url(config["discord"]["webhook"])


def startScanning(product_image, product_title, link, price, status, site, site_img):

    if config["settings"]["start_webhooks"] == True:

        embed = discord.Embed(
            title=f"🔎 STARTED SCANNING",
            color=0x161955,
            timestamp=discord.utils.utcnow(),
            description=product_title,
        )

        embed.set_author(
            name=site.upper(),
            url=f"https://www.{site}.com/",
            icon_url=site_img,
        )  # set author

        embed.set_image(url="")  # set image

        embed.set_thumbnail(url=product_image)  # set thumbnail

        embed.set_footer(
            text="nic#0002",
            icon_url="https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png",
        )  # set footer

        embed.add_field(name="URL", value=link, inline=True)

        embed.add_field(name="PRICE", value=price, inline=True)

        embed.add_field(name="STATUS", value=status, inline=True)

        try:
            webhook.send(content="", embed=embed)

        except Exception as exception:
            print(
                f"{color(style='fail', text='WEBHOOK ERROR: ')} {exception.args[0].args[1].args[1]}"
            )
            exit()


def notify(products, current):

    if config["settings"]["webhooks"] == True:

        embed = discord.Embed(
            title=f"🎉 ITEM INSTOCK",
            color=0xCFC00,
            timestamp=discord.utils.utcnow(),
            description=products.get(current).name,
        )

        embed.set_author(
            name=f"Polyphia",
            url="https://www.polyphia.com/",
            icon_url="https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615",
        )  # set author

        embed.set_image(url="")  # set image

        embed.set_thumbnail(url=products.get(current).img)  # set thumbnail

        embed.set_footer(
            text="nic#0002",
            icon_url="https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png",
        )  # set footer

        embed.add_field(name="URL", value=f"https://www.polyphia.com{products.get(current).url}", inline=False)

        try:

            webhook.send(content=f"<@{config['discord']['my_id']}>", embed=embed)

        except Exception as exception:

            print(
                f"{color(style='fail', text='WEBHOOK ERROR: ')} {exception.args[0].args[1].args[1]}"
            )

            exit()

def newCollection(name, url, site):

    if site == __sites__[0]:

        if config["settings"]["webhooks"] == True:

            embed = discord.Embed(
                title=f"NEW COLLECTION",
                color=0xCFC00,
                timestamp=discord.utils.utcnow(),
                description=name,
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

            embed.add_field(name="URL", value=f"https://www.polyphia.com/{url}", inline=False)

            try:

                webhook.send(content=f"<@{config['discord']['my_id']}>", embed=embed)

            except Exception as exception:

                print(
                    f"{color(style='fail', text='WEBHOOK ERROR: ')} {exception.args[0].args[1].args[1]}"
                )

                exit()
        
    elif site == __sites__[1]: #babymetal

        if config["settings"]["webhooks"] == True:

            embed = discord.Embed(
                title=f"NEW COLLECTION",
                color=0xCFC00,
                timestamp=discord.utils.utcnow(),
                description=name,
            )

            embed.set_author(
                name=f"BABYMETAL",
                url="https://babymetalstore.com/",
                icon_url="https://cdn.shopify.com/s/files/1/2212/1957/files/Baby_Metal_logo_280x@2x.png?v=1613671501",
            )  # set author

            embed.set_image(url="")  # set image

            embed.set_thumbnail(url="")  # set thumbnail

            embed.set_footer(
                text="nic#0002",
                icon_url="https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png",
            )  # set footer

            embed.add_field(name="URL", value=f"https://babymetalstore.com/collections{url}", inline=False)

            try:

                webhook.send(content=f"<@{config['discord']['my_id']}>", embed=embed)

            except Exception as exception:

                print(
                    f"{color(style='fail', text='WEBHOOK ERROR: ')} {exception.args[0].args[1].args[1]}"
                )

                exit()

        print(f"NEW COLLECTION FOUND: {name} -- {url}")


# @nic I removed type from here because I only seeing you use it once, either come up with a better way of doing this or actually add the type everywhere
def dataError(data):

    if config["settings"]["webhooks"] == True:

        try:
            embed = discord.Embed(
                title=f"❌ {type} ERROR {data.status_code}",
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

            try:

                webhook.send(content=f"<@{config['my_id']}>", embed=embed)

            except Exception as exception:

                print(
                    f"{color(style='fail', text='WEBHOOK ERROR: ')} {exception.args[0].args[1].args[1]}"
                )

                exit()

        except Exception as webhookexception:

            print(
                f"{color(style='fail', text='WEBHOOK DATA ERROR: ')} {webhookexception}"
            )

    else:

        print(f"{color(style='fail', text=f'{type} ERROR: ')} {data}")

        exit()
