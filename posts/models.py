from django.db import models


#added lines
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    IMG_TYPE = [
        ("PR", "PORTRAIT"),
        ("LN", "LANDSCAPE"),
        ("SF", "SELFIE"),
        ("AR", "ART"),
        ("DC", "DOCUMENT"),
        ("PN", "PANORAMA"),
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    likes = models.IntegerField(default=0)
    description = models.TextField(default="No Description")
    post_time = models.DateTimeField(default=timezone.now)
    image_type = models.CharField(max_length=2, choices=IMG_TYPE)

    def __str__(self):
        return self.name

# one to many relationships (given by default)
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_likes = models.IntegerField()
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} has commented '{self.content}' on the post {self.post.name}"

# many to many relationship

class Repost(models.Model):
    reposted_by = models.ManyToManyField(User, related_name='Reposts')