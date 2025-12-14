from django.db import models

class Post(models.Model):
    title = models.CharField()
    post = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    # image = models.ImageField(null=True)