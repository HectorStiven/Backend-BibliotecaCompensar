from django.db import models
from datetime import date



class Colegio(models.Model):
    nombre_colegio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono_contacto = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    direccion_web = models.CharField(max_length=100)
    cod_departamento = models.CharField(max_length=10)
    cod_municipio = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_colegio

    class Meta:
        verbose_name = 'Colegio'
        verbose_name_plural = 'Colegios'
        db_table = 'T005colegios'



class Jornada(models.Model):
    cod_jornada = models.CharField(max_length=10, primary_key=True)
    nombre_jornada = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_jornada

    class Meta:
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'
        db_table = 'T007jornadas'


class Grado(models.Model):
    numero_sub_grado = models.CharField(max_length=100, primary_key=True)
    nombre_grado = models.CharField(max_length=100)
    nombre_subgrado = models.CharField(max_length=100)
    cod_jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True, blank=True)
    cod_colegio = models.CharField(max_length=10)
    def __str__(self): 
        return self.nombre_grado

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
        db_table = 'T006grados'




class TipoDocumento(models.Model):
    tipocodigo = models.CharField(max_length=10)
    nombre_codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_codigo

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'
        db_table = 'T008tipos_documento'


class Generos(models.Model):
    codigoGenero = models.CharField(max_length=10)
    nombre_Genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_Genero

    class Meta:
        verbose_name = 'Generos'
        verbose_name_plural = 'Generos'
        db_table = 'T009Genero'




class Estudiante(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento,  on_delete=models.SET_NULL, null=True, blank=True)
    numero_identidad = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, null=True, blank=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, null=True, blank=True)
    edad = models.IntegerField()
    tipo_genero = models.ForeignKey(Generos,  on_delete=models.SET_NULL, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField()
    numero_celular = models.CharField(max_length=15)
    pertenece_colegio = models.BooleanField(default=False)
    colegio = models.ForeignKey(Colegio, on_delete=models.SET_NULL, null=True, blank=True)
    id_grado = models.ForeignKey(Grado, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        db_table = 'T004estudiantes_registrados'





class CategoriaLibros(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    otra_categoria_cual = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        verbose_name = 'Categoría de Libros'
        verbose_name_plural = 'Categorías de Libros'
        db_table = 'T003CategoriaLibros'



class Autor(models.Model):
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, null=True, blank=True)
    primer_apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField()
    numero_celular = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        db_table = 'T002Autores'

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        db_table = 'T012Editoriales'



class Estantes(models.Model):
    # Llave primaria personalizada
    id_estante = models.CharField(max_length=100, primary_key=True)
    identificacion_estante = models.CharField(max_length=100,null=True,blank=True)
    identificacion_por_estante = models.CharField(max_length=100)
    orden_ubicacion_estante = models.IntegerField()
    def __str__(self):
        return self.id_estante

    class Meta:
        verbose_name = 'Estante'
        verbose_name_plural = 'Estantes'
        db_table = 'T011Estantes'



class Libro(models.Model):
    idISBN = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=200)
    categoriaLibro = models.ForeignKey(CategoriaLibros, on_delete=models.PROTECT)
    disponibleEnBiblioteca = models.BooleanField(default=True)
    Editorial = models.ForeignKey(Editorial, on_delete=models.SET_NULL, null=True, blank=True)
    id_Autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    agno_publicacion = models.PositiveIntegerField(null=True,blank=True)  # Año de publicación
    descripcion = models.TextField(null=True,blank=True)  # Descripción
    id_Autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='libros_id_Autor')
    # estado = models.CharField(max_length=100, default='Disponible')  # Estado del libro
    estado_libro = models.BooleanField(default=True)  # Estado del libro, por defecto disponible
    id_estante = models.ForeignKey(Estantes, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad_copias=models.IntegerField(default=1)
    cantidad_inventario=models.IntegerField(default=1)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        db_table = 'T001Libros'



class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    fecha_prestamo = models.DateField( null=True, blank=True)
    fecha_devolucion_libro = models.DateField( null=True, blank=True)
    tiempo_devolucion_dias = models.IntegerField()
    ya_devuelto = models.BooleanField()
    fecha_devolucion_real = models.DateField( null=True, blank=True)
    observaciones_devolucion = models.TextField( null=True, blank=True)
    dias_mora = models.TextField(default=0)  # Valor por defecto como cadena vacía

    def __str__(self):
        return f"Prestamo de {self.libro} a {self.estudiante}"

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        db_table = 'T010Prestamos'



class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    tipoDocumento = models.CharField(max_length=50)
    numeroDocumento = models.CharField(max_length=50)
    tipoUsuario = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    ocupacion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correoElectronico = models.EmailField()
    pais = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    codigoPostal = models.CharField(max_length=10)
    direccion = models.CharField(max_length=200)
    nombreFamiliar = models.CharField(max_length=100)
    celularFamiliar = models.CharField(max_length=15)
    parentesco = models.CharField(max_length=50)
    crearUsuario = models.BooleanField(default=False)
    crearContrasena = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'T013Usuario'
