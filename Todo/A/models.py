from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title