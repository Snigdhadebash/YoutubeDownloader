from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def index(request):
    #Get the link
    youtubeurl = request.POST.get('youtubelink')
    yt = YouTube(youtubeurl)
    title = yt.title
    stream = yt.streams.first()
    
    stream.download('C:/Users/CISPL- SNIHDHADEB/Downloads/youtube video')
    #print(youtubeurl)
    #params={'purpose':'The Url is: ','url':youtubeurl}
    return render(request,'index.html',{'youtubeurl':youtubeurl,'title':title,'stream':stream})
    