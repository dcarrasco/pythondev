from django.db import models
from django.urls import reverse

from pythondev.helpers import Collection
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
    icono = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=100, blank=True)
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

class AppHelper:
    def app_menu():
        modulos = Collection(Rol.objects.all()).flatmap(
            lambda rol: list(rol.modulos.all())
        ).map(lambda modulo: {
            'orden': str(modulo.app.orden)+'.'+str(modulo.orden),
            'app_app': modulo.app.app,
            'app_icono': modulo.app.icono,
            'app_selected': False,
            'mod_modulo': modulo.modulo,
            'mod_llave_modulo': modulo.llave_modulo,
            'mod_icono': modulo.icono,
            'mod_url': modulo.url,
            'mod_selected': False,
        }).sort(
            lambda item: item['orden']
        ).all()

        menu = dict()
        for modulo in modulos:
            modulo_list = {
                'modulo': modulo['mod_modulo'],
                'llave_modulo': modulo['mod_llave_modulo'],
                'icono': modulo['mod_icono'],
                # 'url': reverse(modulo['mod_url']) if modulo['mod_url'] != '' else '',
                'url': '',
                'selected': modulo['mod_selected'],
            }

            if modulo['app_app'] in menu:
                menu[modulo['app_app']]['modulos'].append(modulo_list)
            else:
                menu[modulo['app_app']] = {
                    'app': modulo['app_app'],
                    'icono': modulo['app_icono'],
                    'selected': modulo['app_selected'],
                    'modulos': [modulo_list],
                }

        return menu
