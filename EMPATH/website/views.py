from django.shortcuts import render
from website.models import Video

# Create your views here.
def stories(request):
    #Will Grab all video links here for main page
    videoList = Video.objects.all()
    #print(videoList)
    context = {"videoList":videoList}
    return render(request,'website\\stories.html',context)

def opinions(request):
    return None
def contact(request):
    return None