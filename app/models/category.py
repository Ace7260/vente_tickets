from django.db import models

class Category(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.code} {self.description}"