from django.db import models
from .category import Category
from django.utils import timezone
class Ticket(models.Model):
    categorie = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField( upload_to='tickets', height_field=None, width_field=None, max_length=None)
    status=models.BooleanField()
    date_ajout = models.DateTimeField(default=timezone.now)
    expiration = models.DateTimeField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.description 
    def save(self,*args, **kwargs):
        self.image.save(self.image.name,self.image)
        super().save(*args,**kwargs)
          

