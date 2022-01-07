import pytube
times=int(input("請輸入下載影片數量"))
for i in range(times):

  url=input("影片網址")
  youtube = pytube.YouTube(url)
  video = youtube.streams.get_highest_resolution()
  video.download()