from pytube import YouTube

link = input("YouTube link:")
video = YouTube(link)
quality = input("качествно видео: (High/Low)")
if quality == "High":
    output = video.streams.get_highest_resolution()
if quality == "Low":
    output = video.streams.get_lowest_resolution()

output.download()
