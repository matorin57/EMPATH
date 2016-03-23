from django.shortcuts import render

# Create your views here.
def stories(request):
	#Will Grab all video links here for main page
	context = {}
	render(request,'website\\stories.html',context)