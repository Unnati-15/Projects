
# Register your models here.
from django.contrib import admin
from dog.models import Dogproduct


@admin.register(Dogproduct)
class DogproductAdmin(admin.ModelAdmin):
     pass
