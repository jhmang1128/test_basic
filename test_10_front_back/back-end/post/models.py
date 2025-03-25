from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post")
    
    def __str__(self):
        return self.title