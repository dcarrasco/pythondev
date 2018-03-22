from django.db import models

# Create your models here.

class App(models.Model):
    app = models.CharField('nombre de la aplicacion', max_length=50)
    descripcion = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    icono = models.CharField(max_length=50)
    orden = models.IntegerField()

    def __str__(self):
        return self.app

    class Meta:
        db_table = "acl_app"
        verbose_name = 'aplicacion'
        verbose_name_plural = 'aplicaciones'
        ordering = ["orden"]


class Rol(models.Model):
    app = models.ForeignKey('App', on_delete=models.PROTECT, db_column='id_app')
    rol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    # modulos = models.ManyToManyField('Modulo', through='Rol_modulo', through_fields=('rol', 'modulo'))
    modulos = models.ManyToManyField('Modulo', db_table='acl_rol_modulo')

    def __str__(self):
        return self.rol

    def get_modulos(self):
        return ", ".join([m.modulo for m in self.modulos.all()])

    class Meta:
        db_table = "acl_rol"
        verbose_name_plural = 'roles'
        ordering = ["app", "rol"]


class Modulo(models.Model):
    app = models.ForeignKey('App', on_delete=models.PROTECT, db_column='id_app')
    modulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    llave_modulo = models.CharField(max_length=100)
    icono = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    orden = models.IntegerField()

    def __str__(self):
        return self.modulo

    class Meta:
        db_table = "acl_modulo"
        ordering = ["app", "orden"]


# class Rol_modulo(models.Model):
#     rol = models.ForeignKey('Rol', on_delete=models.PROTECT, db_column='id_rol')
#     modulo = models.ForeignKey('Modulo', on_delete=models.PROTECT, db_column='id_modulo')

#     class Meta:
#         db_table = "acl_rol_modulo"
