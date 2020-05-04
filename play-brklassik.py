import pychromecast

target_device = "Dave's Chromecast"

pychromecast.IGNORE_CEC.append(target_device)  # Ignore CEC on Chromecasts named Living Room
chromecasts = pychromecast.get_chromecasts()

cast = next(cc for cc in chromecasts if cc.device.friendly_name == target_device)

cast.wait()
print(cast.device)
print(cast.status)

mc = cast.media_controller
mc.play_media("https://br-edge-10aa-fra-dtag-cdn.cast.addradio.de/br/brklassik/live/mp3/128/stream.mp3", "audio/mp3")
print(mc.status)
mc.block_until_active()

