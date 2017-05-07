# GPMDP Now Playing Parser

A tiny little Python script for parsing the currently playing track from the [Google Play Music Desktop Client](https://www.googleplaymusicdesktopplayer.com/) into a text file. Useful for streamers!

## Getting Started

Requires [Python 3.0.0+](https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe).

Make sure to enable the "Enable JSON API" and "Enable Playback API" options under the Desktop Settings of the GPMDP client.

Extract both [parser.py](parser.py) and [nowplaying.txt](nowplaying.txt) into a folder, then simply launch [parser.py](parser.py). [nowplaying.txt](nowplaying.txt) will contain then current track title and artist and is updated every 5 seconds.

Terminate the script in the command line with
```
control + c
```

### Configuration

With a little knowledge about Python, [parser.py](parser.py) should be easily understandable to customize to your liking!