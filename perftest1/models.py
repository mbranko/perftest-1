from django.db import models
from django.utils.timezone import now


def sada():
    return now()


class Test(models.Model):
    naziv = models.CharField(max_length=100)
    datum_kreiranja = models.DateField(default=sada)
    datum_vazenja = models.DateField(default=sada)

    def __str__(self):
        return self.naziv + ' ' + self.datum_vazenja.strftime('%Y-%m-%d')

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'testovi'

