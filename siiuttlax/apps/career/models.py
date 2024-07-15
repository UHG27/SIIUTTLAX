from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Career(models.Model):

    LEVEL_CHOICES = (
        ('TSU', 'Tecnico Suooeriro'),
        ('Ing', 'Ingenieria'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestria')
     )

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    status = models.BooleanField(default=True)
    plan = models.CharField(max_length=4)

    def __str__(self):
        return self.short_name
    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.IntegerField()
    total_hours = models.IntegerField()
    weekly_hours = models.IntegerField()
    file = CloudinaryField(
        verbose_name = "Hoja de Asignatura",
        null = True, blank = True,
        resource_type = "pdf",
        folder = "asignatura"
    )
    def __str__(self):
        return f"{ self.name } - { self.Career }"
    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"
