from django.db import models
from .category import Category
from django.utils import timezone
class Ticket(models.Model):
    categorie = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    status=models.BooleanField()
    date_ajout = models.DateTimeField(default=timezone.now)
    expiration = models.DateTimeField(auto_now=False,auto_now_add=False)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.description 

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url             

