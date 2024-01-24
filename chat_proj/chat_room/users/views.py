from django.http import HttpResponse
from django.template import loader
from .models.user import User
import logging

logger = logging.getLogger("django")

def users(request):
  myusers = User.objects.all().values()
  template = loader.get_template('all_users.html')
  context = {
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))

def user_details(request, id):
  myuser = User.objects.get(id=id)
  template = loader.get_template('user_details.html')
  context = {
    'myuser': myuser,
  }
  logger.info(myuser.user_since())
  return HttpResponse(template.render(context, request))

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def chat(request):
  template = loader.get_template('chat.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('testpage.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))