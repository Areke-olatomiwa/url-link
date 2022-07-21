from django.db import models

from django.contrib.auth import get_user_model
User=get_user_model()
class Link(models.Model):
    objects = None
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.target_url


