from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Room)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Type)


