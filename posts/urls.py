from django.contrib import admin
from django.urls import path

# added lines
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

#added line, creates namespace for the app
app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('post/', views.posts, name="post"),
    path('<int:post_id>/', views.post_details, name="post_details"),
]
