from django.db import models

class User(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  username = models.CharField(max_length=255, null=True)
  joined_date = models.DateField(null=True)