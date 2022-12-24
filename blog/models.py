from django.db import models
from accounts.models import Account


class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
