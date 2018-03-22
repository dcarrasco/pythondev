from django.db import models

# Create your models here.
class Almacen(models.Model):
    almacen = models.CharField('codigo de almacen', max_length=10, primary_key=True)

    def __str__(self):
        return self.almacen

    class Meta:
        db_table = "fija_almacenes"
        verbose_name_plural = 'almacenes'
        ordering = ["almacen"]


class Auditor(models.Model):
    nombre = models.CharField('nombre del auditor', max_length=50)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "fija_auditores"
        verbose_name_plural = 'auditores'
        ordering = ["nombre"]


class Catalogo(models.Model):
    catalogo = models.CharField('codigo del catalogo', max_length=20, primary_key=True)
    descripcion = models.CharField('descripcion del catalogo', max_length=50)
    pmp = models.FloatField('valor del catalogo')
    es_seriado = models.BooleanField()

    def __str__(self):
        return self.catalogo + ' - ' + self.descripcion

    class Meta:
        db_table = "fija_catalogos"
        ordering = ["catalogo"]


class Centro(models.Model):
    centro = models.CharField('codigo del centro', max_length=10, primary_key=True)

    def __str__(self):
        return self.centro

    class Meta:
        db_table = "fija_centros"
        ordering = ["centro"]


class Familia(models.Model):
    TIPOS = (
        ('FAM', 'Familia'),
        ('SUBFAM', 'SubFamilia')
    )
    codigo = models.CharField('codigo', max_length=50, primary_key=True)
    tipo = models.CharField('familia o subfamilia', max_length=30, choices=TIPOS)
    nombre = models.CharField('nombre', max_length=50)

    def __str__(self):
        return self.codigo + ' - ' + self.nombre

    class Meta:
        db_table = "fija_familias"
        ordering = ["codigo"]


class Inventario(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre del inventario. Maximo 50 caracteres")
    activo = models.BooleanField()
    tipo_inventario = models.ForeignKey('Tipo_inventario', on_delete=models.PROTECT, db_column='tipo_inventario')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "fija_inventarios"
        ordering = ["nombre"]


class Tipo_inventario(models.Model):
    id_tipo_inventario = models.CharField('id', max_length=10, primary_key=True)
    desc_tipo_inventario = models.CharField('descripcion', max_length=50)

    def __str__(self):
        return self.desc_tipo_inventario

    class Meta:
        db_table = "fija_tipos_inventario"
        verbose_name = 'tipo de inventario'
        verbose_name_plural = 'tipos de inventario'
        ordering = ["desc_tipo_inventario"]


class Tipo_ubicacion(models.Model):
    tipo_inventario = models.ForeignKey('Tipo_inventario', on_delete=models.PROTECT, db_column='tipo_inventario')
    tipo_ubicacion = models.CharField('tipo de ubicacion', max_length=30)

    def __str__(self):
        return self.tipo_ubicacion

    class Meta:
        db_table = "fija_tipo_ubicacion"
        verbose_name = 'tipo de ubicacion'
        verbose_name_plural = 'tipos de ubicacion'
        ordering = ["tipo_inventario", "tipo_ubicacion"]


class Unidad_medida(models.Model):
    unidad = models.CharField('codigo', max_length=10, primary_key=True)
    desc_unidad = models.CharField('descripcion', max_length=50, unique=True)

    def __str__(self):
        return self.desc_unidad

    class Meta:
        db_table = "fija_unidades"
        verbose_name = 'unidad de medida'
        verbose_name_plural = 'unidades de medida'
        ordering = ["unidad"]

class DetalleInventario(models.Model):
    id_inventario = models.ForeignKey('Inventario', on_delete=models.PROTECT, db_column='id_inventario')
    ubicacion = models.CharField(max_length=10)
    catalogo = models.ForeignKey('Catalogo', on_delete=models.PROTECT, db_column='catalogo')
    descripcion = models.CharField(max_length=45)
    lote = models.CharField(max_length=10)
    lote = models.CharField(max_length=10)
    centro = models.ForeignKey('Centro', on_delete=models.PROTECT, db_column='centro')
    almacen = models.ForeignKey('Almacen', on_delete=models.PROTECT, db_column='almacen')
    um = models.ForeignKey('Unidad_medida', on_delete=models.PROTECT, db_column='um')
    stock_sap = models.IntegerField()
    stock_fisico = models.IntegerField()
    digitador = models.IntegerField()
    auditor = models.IntegerField()
    hoja = models.IntegerField()
    reg_nuevo = models.CharField(max_length=1)
    observacion = models.CharField(max_length=200)
    fecha_modificacion = models.DateField()
    stock_ajuste = models.IntegerField()
    glosa_ajuste = models.CharField(max_length=100)
    fecha_ajuste = models.DateField()
    hu = models.CharField(max_length=20)

    def __str__(self):
        return str(self.catalogo)

    class Meta:
        db_table = "fija_detalle_inventario"
        verbose_name = 'detalle de inventario'
        verbose_name_plural = 'detalles de inventario'
        ordering = ["id_inventario", "hoja", "ubicacion", "catalogo"]
