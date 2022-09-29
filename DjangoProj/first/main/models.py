from django.db import models
from django.core import validators
# class Cars(models.Model):
#     title = models.CharField(max_length= 150)
#     price = models.DecimalField(max_digits= 12, decimal_places= 2)
#     description = models.TextField(blank = True)
#     phone = models.CharField(max_length= 30)
#     owner = models.CharField(max_length= 50)

    # class Meta:
    #     verbose_name = 'Car'
    #     verbose_name_plural = 'Cars'
    #
    # def __str__(self):
    #     return self.title


class Musician(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Song(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Musician, on_delete=models.CASCADE,
                               related_name='songs')
    feat = models.ForeignKey(Musician, on_delete=models.CASCADE, null=True,
                             related_name='feats', blank=True)
    poster = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='songs/', blank=True,validators=[validators.FileExtensionValidator(['mp3'], message='file must be mp3')])
    video = models.FileField(upload_to='video/', blank=True,validators=[validators.FileExtensionValidator(['mp4'], message='file must be mp4')])

    year = models.DateField()

    def __str__(self):
        if self.feat:
            return f'{self.author} - {self.title} feat {self.feat}'
        return f'{self.author} - {self.title}'
