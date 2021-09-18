from pytube import YouTube

# YouTube("https://www.youtube.com/watch?v=ibs2bE0jyxQ").streams.first().download()

yt = YouTube("https://www.youtube.com/watch?v=ibs2bE0jyxQ")

yt.streams.filter(progressive=True, file_extension="mp4")

yt.streams.order_by('resolution')

yt.streams.first().download()



