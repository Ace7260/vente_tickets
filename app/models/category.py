from django.db import models

class Category(models.Model):
    code = models.CharField(max_length=50, null=True)
    description = models.CharField(null=False, max_length=50,unique=True)

    def __str__(self):
        return f"{self.code} {self.description}"