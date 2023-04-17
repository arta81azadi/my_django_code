from django.contrib import auth
from django.db import models
from django.urls import reverse


class Post(models.Model):
    STATUS = (
        ('PUB', 'public'),
        ('DRA', 'draft'),
    )

    title = models.CharField(max_length=101)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    deta_created = models.DateTimeField(auto_now_add=True)
    deta_edited = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
