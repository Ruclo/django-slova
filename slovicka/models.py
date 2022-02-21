from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings

# Create your models here.

class Cvicenie(models.Model):
    nazov = models.CharField(max_length=50)
    datum = models.DateTimeField('Datum uverejnenia')
    groups = tuple(Group.objects.all())
    vyber = zip(map(str,groups),map(str,groups))
    trieda = models.CharField(max_length=100, choices=vyber)

    def __str__(self):
        return self.nazov

    class Meta:
        verbose_name_plural = 'Cvicenia'


class Slovicko(models.Model):
    jazyk1 = models.CharField(max_length=30)
    jazyk2 = models.CharField(max_length=30)
    cvicenie = models.ForeignKey(Cvicenie,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.jazyk1} - {self.jazyk2}'

    class Meta:
        verbose_name_plural = 'Slovicka'


class Pokus(models.Model):
    ziak = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cvicenie = models.ForeignKey(Cvicenie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ziak} - {self.cvicenie}'

    class Meta:
        verbose_name_plural = 'Pokusy'


class Odpoved(models.Model):
    ziak = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pokus = models.ForeignKey(Pokus, on_delete=models.CASCADE)
    spravne = models.CharField(max_length=100,default = 'default')
    odpoved = models.CharField(max_length=100)
    jespravne = models.BooleanField(default=None)

    def __str__(self):
        #return self.odpoved
        return self.spravne

    class Meta:
        verbose_name_plural = 'Odpovede'
