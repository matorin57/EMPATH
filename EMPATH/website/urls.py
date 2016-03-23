#contains url mathces
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.stories, name='index'),
	url(r'^stories/$', views.stories, name='index'),
]