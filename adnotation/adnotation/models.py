from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')
    upload_date = models.DateTimeField(auto_now_add=True)

class AnnotatedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    json_data = models.JSONField()
    uploaded_at = models.DateTimeField(auto_now_add=True)



def __str__(self):
    return self.name
