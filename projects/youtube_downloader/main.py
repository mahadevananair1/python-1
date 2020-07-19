import pytube

link = input('Enter a link: ')
yt = pytube.YouTube(link)

videos = yt.streams.all()
i = 1
for stream in videos:
    print(str(i) +''+ str(stream))
    i += i

stream_number = int(input('Enter nuumber: '))
video = videos[stream_number - 1]
video.download("/home/jan/Downloads")

print("Downloaded")

