from pytube import YouTube

link = input("Input youtube link:")
video = YouTube(link)
quality = input("качествно видео: (High/Low)")
output = None
if quality == "High":
    output = video.streams.get_highest_resolution()
if quality == "Low":
    output = video.streams.get_lowest_resolution()

output.download()
