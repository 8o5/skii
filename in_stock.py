import time

import requests
from bs4 import BeautifulSoup
import toml
from discord_webhook import DiscordEmbed, DiscordWebhook

config = toml.load("config.toml")

webhook = DiscordWebhook(
                        url=config['webhook']
    )

def notify():

    embed = DiscordEmbed(
                            title=f'🎉 ITEM INSTOCK', description='', color='7CFC00')

    embed.set_author(name=f"Polyphia", url='https://www.polyphia.com/',
                    icon_url='https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615')  # set author

    embed.set_image(url='')  # set image

    embed.set_thumbnail(url='https://cdn.shopify.com/s/files/1/0271/6018/2883/products/WHITE_SILVERSMUSH_1024x1024@2x.png?v=1662044356')  # set thumbnail

    embed.set_footer(text='nic#0002',
                    icon_url='https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png')  # set footer

    embed.set_timestamp()  # set timestamp (default is now)

    embed.add_embed_field(name='URL', value=f"{config['url']}s", inline=False)

    webhook.add_embed(embed)
    webhook.set_content(f"<@{config['my_id']}>")
    webhook.execute()


def check(url, headers):

    data = requests.get(
        url,
        headers,
        timeout=5,
    )


    data.raise_for_status()


    if data.status_code != 200:
        embed = DiscordEmbed(
                            title=f'❌ ERROR {data.status_code}', description=f'@{config["my_id"]}', color='EE4B2B')

        embed.set_author(name=f"Polyphia", url='https://www.polyphia.com/',
                        icon_url='https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615')  # set author

        embed.set_image(url='')  # set image

        embed.set_thumbnail(url='')  # set thumbnail

        embed.set_footer(text='nic#0002',
                        icon_url='https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png')  # set footer

        embed.set_timestamp()  # set timestamp (default is now)

        embed.add_embed_field(name='URL', value=f"{config['url']}s", inline=False)

        webhook.add_embed(embed)
        webhook.set_content(f"<@{config['my_id']}>")
        webhook.execute()

        print(data.status_code)
        exit()

    elif data.status_code == 200:

        x = BeautifulSoup(data.content, "html.parser")

        status = x.find(attrs={"aria-label": "Sold out"})
            
        if status is None:
            notify()
            time.ctime()
            print(
                f"[{time.ctime()}] -- INSTOCK"
            )
            return
        else:
            time.ctime()
            print(
                f"[{time.ctime()}] -- OOS"
            )


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

print(
    f"SCANNING {config['url']}"
)

embed = DiscordEmbed(
                        title=f'🔎 STARTED SCANNING', description='', color='161955')

embed.set_author(name=f"Polyphia", url='https://www.polyphia.com/',
                icon_url='https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615')  # set author

embed.set_image(url='')  # set image

embed.set_thumbnail(url='https://cdn.shopify.com/s/files/1/0271/6018/2883/products/WHITE_SILVERSMUSH_1024x1024@2x.png?v=1662044356')  # set thumbnail

embed.set_footer(text='nic#0002',
                icon_url='https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png')  # set footer

embed.set_timestamp()  # set timestamp (default is now)

embed.add_embed_field(name='URL', value=f"{config['url']}s", inline=False)

webhook.add_embed(embed)
webhook.set_content(f"<@{config['my_id']}>")
webhook.execute()

while True:
    check(
        url=config['url'], 
        headers=headers,
        )
    time.sleep(60)