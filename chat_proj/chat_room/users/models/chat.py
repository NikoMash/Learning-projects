from django.db import models

class Chat(models.Model):
    title = models.CharField(max_length=500)
    info = models.CharField()