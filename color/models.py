from django.db import models
from colorfield.fields import ColorField


class Palette(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Палитра'
        verbose_name_plural = 'Палитры'

    def __str__(self):
        return self.name


class Color(models.Model):
    hex = ColorField()
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name
