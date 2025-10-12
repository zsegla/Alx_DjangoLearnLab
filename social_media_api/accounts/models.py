

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following',  # users that this user follows
        blank=True
    )

    def __str__(self):
        return self.username







# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     bio = models.TextField(blank=True, null=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#     followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
#     following = models.ManyToManyField('self',symmetrical=False, related_name='followers')
#     def __str__(self):
#         return self.username
