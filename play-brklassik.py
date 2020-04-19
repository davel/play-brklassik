import pychromecast

chromecasts = pychromecast.get_chromecasts()

cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Dave's Chromecast")
cast.wait()
print(cast.device)
print(cast.status)
cast.media_controller.play_media("https://br-edge-10aa-fra-dtag-cdn.cast.addradio.de/br/brklassik/live/mp3/128/stream.mp3", "audio/mp3")
