from django.db import models

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=100, blank=False, default='None')

    def __str__(self):
        return self.name

  
class Projeto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    tecnology = models.CharField(max_length=100)
    descrition = models.TextField()
    image = models.ImageField(upload_to='projetos/%y/%m/%d', blank=True)
    concluido = models.BooleanField(default=True, auto_created=True)

    def __str__(self):
        return self.name


