from django.db import models

class Cars(models.Model):
    title = models.CharField(max_length= 150)
    price = models.DecimalField(max_digits= 12, decimal_places= 2)
    description = models.TextField(blank = True)
    phone = models.CharField(max_length= 30)
    owner = models.CharField(max_length= 50)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.title