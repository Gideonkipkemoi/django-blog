from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Apply(models.Model):
    name = models.CharField(max_length=20)
    admission_no = models.CharField(max_length=20)
    email_address = models.EmailField()
    institution = models.CharField(max_length=20)
    Period = models.IntegerField(default=6)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title





    def get_absolute_url(self):
        return reverse('home')
