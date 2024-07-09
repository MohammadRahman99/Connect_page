from django.contrib import admin

# Register your models here.
from main_app.models import *
admin.site.register(UserInfo)
admin.site.register(Experience)
admin.site.register(ContactInfo)