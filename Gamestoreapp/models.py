from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    number = models.IntegerField()
    cat = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    
