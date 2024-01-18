from django.db import models

# Create your models here.
class Dogproduct(models.Model):
         image= models.ImageField(upload_to="static/images",default="")
         name = models.CharField(max_length=100)
         description = models.TextField()
         price = models.IntegerField()
         desc = models.TextField(default='SOME STRING')
         quantity = models.IntegerField()
         class Meta:
               verbose_name_plural = "Products"
         def __str__(self):
                return f"{self.name}"


  