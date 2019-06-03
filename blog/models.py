from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=False)
    content = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def pub_date_clean(self):
        return self.pub_date.strftime('%b %e %Y')