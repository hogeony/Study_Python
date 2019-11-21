from pytube import Playlist

url_youtube_playlist = 'https://www.youtube.com/playlist?list=PLC1qU-LWwrF64f4QKQT-Vg5Wr4qEE1Zxk'

playlist = Playlist(url_youtube_playlist)
print('Number of videos in playlist: %s' % len(playlist.video_urls))
playlist.download_all()
