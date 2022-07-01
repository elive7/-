from django.db import models

# Create your models here.

class Comment(models.Model):
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment

