"""Models for Posts """
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
#Import model profile
from users.models import Profile

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="posts/photos")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)

    user =  models.ForeignKey(User,on_delete=CASCADE)
    profile = models.ForeignKey(Profile,on_delete=CASCADE)


    def __str__(self):
        return '{} by @ {} '.format(self.title, self.user.username)