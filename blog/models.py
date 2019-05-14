from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=False)
    content = models.TextField()
