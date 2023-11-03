#匯入模組
from pytube import YouTube

#進度條函式(串流,還沒寫入硬體的資訊,還有多少沒下載完)
def show(stream , chunk , bytes_remaining):
    #影片大小
    size = stream.filesize

    #目前進度
    temp = (size - bytes_remaining)*100 /size
    
    #印出
    print('目前進度' ,temp ,'%')

#建立物件
#yt = YouTube('五分鐘以內的youtube影片網址')
yt = YouTube('https://www.youtube.com/watch?v=ku3-0AyUy_g&ab_channel=TEENTOPOfficial',on_progress_callback = show)

#選擇yt變數裡所有串流中的第一個串流
#filter篩選器 res解析度 fps貞率 only_audio = True 只要聲音
video = yt.streams.filter(res='1080p').first()

#下載
video.download()

