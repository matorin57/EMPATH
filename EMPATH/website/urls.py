#contains url mathces
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.stories, name='index'),
	url(r'^stories/$', views.stories, name='stories'),
    url(r'^opinions/$', views.opinions, name='opinions'),
    url(r'^contact/$', views.contact, name='contact'),
]