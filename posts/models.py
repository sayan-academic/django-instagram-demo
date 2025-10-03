from django.db import models
from django.utils import timezone

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