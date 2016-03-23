from django.db import models

# Create your models here.
#
class Video(models.Model):
	youtubeId = models.TextField()
	name = models.TextField()
	description = models.TextField()
	dateAdded = models.DateField()