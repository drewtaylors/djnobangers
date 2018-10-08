import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class YTVideo(models.Model):
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    next_url = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    text = models.TextField(default='')
