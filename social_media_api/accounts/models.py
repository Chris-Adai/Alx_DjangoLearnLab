from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# class User(AbstractUser):
#     bio = models.TextField(blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
#     followers = models.ManyToManyField('self', symmetrical=False, blank=True)
#         # Add a ManyToManyField for following relationships
#     following = models.ManyToManyField(
#         'self',
#         symmetrical=False,
#         related_name='followers',
#         blank=True
#     )

#     def __str__(self):
#         return self.username

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)
        # Add a ManyToManyField for following relationships
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username

#
# filepath: c:\DJANGO-PROJECTS\ALX_PROJECTS\social_media_api\accounts\models.py
# from django.db import models

# User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
    

