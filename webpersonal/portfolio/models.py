from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField()
    image = models.ImageField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural  = "proyectos"
        ordering = ["-created"]

    def __str___(self):
        return self.title