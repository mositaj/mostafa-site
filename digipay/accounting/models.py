from django.db import models

class TODO(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField()
    

