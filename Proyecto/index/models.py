from django.db import models
from django.utils import timezone

class User(models.Model):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    def guardar(self):
        self.save()

    def name(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='img')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title