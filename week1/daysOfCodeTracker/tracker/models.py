from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    def __str__(self):
        return f'name: {self.name} - \
                 lastname: {self.lastname} - \
                 email: {self.email} - \
                 password: {self.password}'

class Commits(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    date = models.DateField(max_length=40)

    def __str__(self):
        return f'title: {self.title} - \
                 description: {self.description} - \
                 author: {self.author} - \
                 date: {self.date}'
