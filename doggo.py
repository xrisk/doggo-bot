import discord
import asyncio
from imgurpython import ImgurClient
import http.server
import threading
import os

client = discord.Client()

client_id = 'f18a414afc7255c'
client_secret = '3b0f84936e7e2ae5a7f0f5ad6463319b6a779882'

imgur = ImgurClient(client_id, client_secret)


@client.event
async def on_message(message):
    if message.content.startswith('+dog'):
        em = discord.Embed()
        image = imgur.upload_from_url('http://www.randomdoggiegenerator.com/randomdoggie.php')
        em.set_image(url=image['link'])
        await client.send_message(message.channel, embed=em)
    elif message.content.startswith('+jack'):
        em = discord.Embed()
        em.set_image(url='https://cdn.discordapp.com/attachments/97601590860464128/255385870092206080/jack.jpg')
        await client.send_message(message.channel, embed=em)


threading.Thread(target=http.server.test(http.server.SimpleHTTPRequestHandler, port=int(os.getenv('PORT', 5000)))).start()
client.run('MjU1MzYyNTAxMjc1ODExODQy.CyciSA.EKkflsjdmeSt21HTbBd-A98Ijf0')
