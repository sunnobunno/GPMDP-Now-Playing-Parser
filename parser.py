import json
import time

with open('nowplaying.txt', 'r+') as nowplaying:
	while True:
		print 'opening'
		json_data = open('C:\Users\Sunny\AppData\Roaming\Google Play Music Desktop Player\json_store\playback.json')
		print 'reading'
		playback = json.loads(json_data.read())
		title = str(playback['song']['title']).lstrip('u')
		artist = str(playback['song']['artist']).lstrip('u')
		track = '| {} - {} |'.format(title, artist)
		nowplaying.seek(0)
		print 'writing {}'.format(track)
		nowplaying.write(track)
		print 'truncating'
		nowplaying.truncate()
		print 'closing'
		json_data.close()
		time.sleep(5)