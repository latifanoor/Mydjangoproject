from django.contrib import admin

# Register your models here.
from .models import Members,Board,Topic,Post
admin.site.register(Members)
admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)