from django.db import models

# Create your models here.


class Best(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField(upload_to='images/')
class Top(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField(upload_to='images/')
class Quality(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField(upload_to='images/')








class Text_to_Youtube(models.Model):
    name = models.CharField(max_length=250)
    text_wrap = models.TextField()
    text = models.TextField()
    url = models.URLField()
    img = models.ImageField(upload_to='images/')

class Course(models.Model):
    img = models.ImageField(upload_to='images/')
    course_name = models.CharField(max_length=50)
    info = models.TextField()
    teachers_icon = models.ImageField(upload_to='images/')

class Course_Regis(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()