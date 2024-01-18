from django.db import models

# Create your models here.

class Catproduct(models.Model):
         image= models.ImageField(upload_to="static/images",default="")
         name = models.CharField(max_length=100)
         description = models.TextField()
         price = models.IntegerField()
         desc = models.TextField(default='SOME STRING')
         class Meta:
               verbose_name_plural = "Cat_Products"
         def __str__(self):
                return f"{self.name}"      