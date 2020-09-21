import sys
import pychromecast
import urllib

target_device = "Dave's Chromecast"

url = "https://br-brklassik-live.cast.addradio.de/br/brklassik/live/mp3/high"

if len(sys.argv) > 0:
    url = sys.argv[1]

req_head =  urllib.request.Request(url, method="HEAD")

resp = urllib.request.urlopen(req_head)

fmt = resp.getheader("Content-Type")

pychromecast.IGNORE_CEC.append(target_device)  # Ignore CEC on Chromecasts named Living Room
chromecasts = pychromecast.get_chromecasts()

cast = next(cc for cc in chromecasts if cc.device.friendly_name == target_device)

cast.wait()
print(cast.device)
print(cast.status)

mc = cast.media_controller

mc.play_media(url, fmt)

print(mc.status)
mc.block_until_active()

