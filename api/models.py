from django.db import models # type: ignore

# Create your models here.
class Generos(models.Model):
    genero_id = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=225)
    
    class Meta:
        db_table = "generos"


class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    fk_generos = models.ForeignKey(Generos, on_delete=models.CASCADE,default=0)
    class Meta:
        db_table = "usuarios"