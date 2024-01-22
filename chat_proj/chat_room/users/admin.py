from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
  list_display = ("username", "joined_date",)
  
admin.site.register(User, UserAdmin)