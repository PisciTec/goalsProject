from django.contrib import admin
from .models import Post
from .models import Goal
from .models import Start_Value
# Register your models here.



admin.site.register(Post)
admin.site.register(Goal)
admin.site.register(Start_Value)