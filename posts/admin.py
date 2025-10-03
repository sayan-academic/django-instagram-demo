from django.contrib import admin

#added line
from .models import Post

# Register your models here.

admin.site.register(Post)
