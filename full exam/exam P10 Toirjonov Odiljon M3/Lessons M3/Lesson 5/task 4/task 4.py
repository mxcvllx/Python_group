from pytube import YouTube

link = input('Введите ссылка на видео ютуб ->')

yt = YouTube(link)

print(f"youtube video title ->{yt.title}")
print(f"number of views ->{yt.views}")
print(f"video duration ->{yt.length}")

y = yt.streams.get_highest_resolution()
y.download()
print("loading is complete")


