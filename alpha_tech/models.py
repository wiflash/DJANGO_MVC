from django.db import models

# Create your models here.
class Blog(models.Model):
    picture = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=100, default="")
    date = models.DateField(auto_now_add=True)
    content = models.TextField(default="")
    comment = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Mentor(models.Model):
    profile_pic = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=50, default="")
    experience = models.CharField(max_length=50, default="")
    year_exp = models.IntegerField(default=0)
    quotes = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name

class Mentee(models.Model):
    profile_pic = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=50, default="")
    quotes = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name