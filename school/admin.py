from django.contrib import admin
from .models import Post,Photo,File

# Register your models here.
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(File)