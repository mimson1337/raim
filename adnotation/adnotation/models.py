from django.db import models

class Photo(models.Model):
    # Model reprezentujący zdjęcia.
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')
    upload_date = models.DateTimeField(auto_now_add=True)

class AnnotatedImage(models.Model):
    # Model reprezentujący obrazy z adnotacjami.
    image = models.ImageField(upload_to='images/')
    json_data = models.JSONField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Annotation(models.Model):
    # Model reprezentujący adnotacje na obrazach.
    image = models.ImageField(upload_to='images/')
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    text = models.CharField(max_length=255)
    height_cm = models.FloatField()
    width_cm = models.FloatField()

    def to_dict(self):
        # Metoda konwertująca adnotację na słownik.
        return {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'text': self.text,
            'heightCm': self.height_cm,
            'widthCm': self.width_cm
        }

    def __str__(self):
        # Metoda zwracająca czytelną reprezentację adnotacji.
        return self.text
