import json
import time

with open('nowplaying.txt', 'r+') as nowplaying:
	while True:
		playback = json.loads(open('C:\Users\Sunny\AppData\Roaming\Google Play Music Desktop Player\json_store\playback.json').read())
		title = str(playback['song']['title']).lstrip('u')
		artist = str(playback['song']['artist']).lstrip('u')
		track = '| {} - {} |'.format(title, artist)
		nowplaying.seek(0)
		nowplaying.write(track)
		nowplaying.truncate()
		#print 'writing'
		time.sleep(5)