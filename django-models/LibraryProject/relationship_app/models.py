
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# UserProfile model to extend User with role
class UserProfile(models.Model):
	ROLE_CHOICES = [
		('Admin', 'Admin'),
		('Librarian', 'Librarian'),
		('Member', 'Member'),
	]
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.CharField(max_length=20, choices=ROLE_CHOICES)

	def __str__(self):
		return f"{self.user.username} ({self.role})"

# Signal to create UserProfile automatically
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance, role='Member')

from django.db import models

# Author Model
class Author(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

# Book Model
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

	def __str__(self):
		return self.title

# Library Model
class Library(models.Model):
	name = models.CharField(max_length=100)
	books = models.ManyToManyField(Book, related_name='libraries')

	def __str__(self):
		return self.name

# Librarian Model
class Librarian(models.Model):
	name = models.CharField(max_length=100)
	library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

	def __str__(self):
		return self.name
