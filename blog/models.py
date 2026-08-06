from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200,blank=False)
    slug = models.SlugField(max_length=50,unique=True,blank=True)
    content=models.TextField(blank=False)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    featured_image=models.ImageField(upload_to='images/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        while Post.objects.filter(slug=self.slug).exists():
            self.slug = f"{self.slug}-{Post.objects.filter(slug__startswith=self.slug).count() + 1}"
        super().save(*args, **kwargs)
    
class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    content=models.TextField(blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'


    