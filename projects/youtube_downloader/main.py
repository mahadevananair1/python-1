import pytube

save_path = '/home/jan/Downloads'
link = input('Enter a link: ')

for i in link:
    youtube = pytube.YouTube(link)
    video = youtube.streams.first()
    video.download(save_path)

print("Task Completed!")
