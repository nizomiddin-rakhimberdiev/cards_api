from django.db import models

# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='card_img/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title