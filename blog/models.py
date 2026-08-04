from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200,blank=False)
    slug = models.SlugField(max_length=50,unique=True)
    content=models.TextField(blank=False)
    author=models.CharField(max_length=100,blank=False)
    category=models.CharField(max_length=100,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



    