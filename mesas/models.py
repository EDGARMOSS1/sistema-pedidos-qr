from django.db import models


class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    descripcion = models.CharField(max_length=100, blank=True)
    activa = models.BooleanField(default=True)
    qr_generado = models.BooleanField(default=False)
    qr_imagen = models.ImageField(upload_to='qr_mesas/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mesa {self.numero}"