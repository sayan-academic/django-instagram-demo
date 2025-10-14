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
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commented_by')
    comment_likes = models.IntegerField()
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} has commented '{self.content}' on the post {self.post.name}"


# many to many relationship
class Repost(models.Model):
    user = models.ManyToManyField(User, related_name='reposted_by')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='repost_post')
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"repost of {self.post.name} by {self.user.count()} people"

# one to one relationship
class Filter(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='filter')
    FILTER_CHOICES = [
        ('BW', 'BLACKANDWHITE'),
        ('GS', 'GRAYSCALE'),
        ('SP', 'SEPIA'),
        ('CR', 'CHROMA'),
        ('RJ', 'RIODEJANEIRO'),
    ]

    filter_type = models.CharField(max_length=2, choices=FILTER_CHOICES)

    #built in method to return the whole field name:::: self.get_<fieldname>_display()
    def __str__(self):
        return self.get_filter_type_display()
    