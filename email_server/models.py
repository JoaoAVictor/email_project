from django.db import models

# Create your models here.

class Email(models.Model):
    recipient = models.EmailField()
    topic = models.CharField(max_length=200)
    message = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True);