import pytube

save_path = '/home/jan/Downloads'

link = input('Enter a link: ')

for i in link:
    try:
        yt = Youtube(i)
    except:
        print("Connection Error")

    yt = yt.get('mp4', '720p')

    try: 
        yt.download(save_path)
    except:
        print("Some Error!")

print("Task Completed!")
