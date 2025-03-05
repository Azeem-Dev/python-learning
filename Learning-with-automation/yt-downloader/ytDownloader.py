from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

print(yt.thumbnail_url,yt.author)

# yt = YouTube(link)

# print(f"Title:{yt.title}")
# print(f"Views:{yt.views}")

# yd = yt.streams.get_highest_resolution()


# YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download("C:/Users/HP/Downloads")
# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("C:/Users/HP/Downloads")
 