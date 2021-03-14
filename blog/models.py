from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    image= models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=300)


    def sum(self):
        return self.summary[:50]

    def __str__(self):
        return self.title    