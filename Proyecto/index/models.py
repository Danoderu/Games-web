from django.db import models

class User(models.Model):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def name(self):
        return self.name

    def guardar(self):
        self.save()


