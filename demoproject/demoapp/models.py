from django.db import models

# Create your models here.
class Place(models.Model):
    Image=models.ImageField(upload_to='pics')
    Name=models.CharField(max_length=250)
    Description=models.TextField()
    def __str__(self):
        return self.Name
