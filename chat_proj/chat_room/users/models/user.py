from django.db import models
import datetime
import logging

logger = logging.getLogger("django")

class User(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  username = models.CharField(max_length=255, null=True)
  joined_date = models.DateField(null=True)

  def user_since(self):
    now_date = datetime.datetime.now().date()
    delta = now_date - self.joined_date
    return delta