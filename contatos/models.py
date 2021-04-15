from django.db import models

class Contato(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField()
    motiv = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.name