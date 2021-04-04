import sys
import pychromecast
import aiohttp
import asyncio

target_device = "Dave's new Chromecast"

url = "https://br-brklassik-live.cast.addradio.de/br/brklassik/live/mp3/high"

if len(sys.argv) > 1:
    url = sys.argv[1]

async def main(url):
   async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status >= 300 and response.status <= 304:
                print("Bouncing to {}".format(response.headers['Location']))
                await main(response.headers['Location'])
            elif response.status == 200:
                print("Have 200!")
                print(response.headers['Content-Type'])
                return response.headers['Content-Type']
            else:
                raise Exception("Bad status {}".format(response.status))

fmt = loop = asyncio.get_event_loop()
loop.run_until_complete(main(url))

print(fmt)

pychromecast.IGNORE_CEC.append(target_device)  # Ignore CEC on Chromecasts named Living Room

services, browser = pychromecast.discovery.discover_chromecasts()
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[target_device])

print(chromecasts)
cast = chromecasts[0] if len(chromecasts)==1 else next(cc for cc in chromecasts if cc.device.friendly_name == target_device)

cast.wait()
print(cast.device)
print(cast.status)

mc = cast.media_controller

mc.play_media(url, fmt)

print(mc.status)
mc.block_until_active()

