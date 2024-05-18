from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    session_id = models.CharField(max_length=36)
    timestamp = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)


    def __str__(self):
        return f'{self.sender}: {self.content[:20]}'