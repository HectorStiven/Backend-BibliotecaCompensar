from django.db import models

class Universidad(models.Model):
    nombre_universidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono_contacto = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    direccion_web = models.CharField(max_length=100)
    cod_departamento = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_universidad

    class Meta:
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'
        db_table = 'T006universidades'



class Colegio(models.Model):
    nombre_colegio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono_contacto = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    cod_departamento = models.CharField(max_length=10)
    cod_municipio = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_colegio

    class Meta:
        verbose_name = 'Colegio'
        verbose_name_plural = 'Colegios'
        db_table = 'T009colegios'



class Jornada(models.Model):
    cod_jornada = models.CharField(max_length=10, primary_key=True)
    nombre_jornada = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_jornada

    class Meta:
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'
        db_table = 'T012jornadas'


class Grado(models.Model):
    nombre_grado = models.CharField(max_length=100)
    nombre_subgrado = models.CharField(max_length=100)
    cod_jornada = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_grado

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
        db_table = 'T010grados'



class GradosColegiosClavesForaneas(models.Model):
    id_colegio = models.OneToOneField(Colegio, primary_key=True, on_delete=models.CASCADE)
    id_grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_colegio} - {self.id_grado}"

    class Meta:
        verbose_name = 'Grados Colegios'
        verbose_name_plural = 'Grados Colegios'
        db_table = 'T013GradosColegios'

class SubGrados(models.Model):
    numero_sub_grado = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.numero_sub_grado

    class Meta:
        verbose_name = 'SubGrado'
        verbose_name_plural = 'SubGrados'
        db_table = 'T011subgrados'


class GradoSubGrado(models.Model):
    id_subgrado = models.OneToOneField(SubGrados, on_delete=models.CASCADE, primary_key=True, db_column='numero_sub_grado')
    id_grado = models.OneToOneField(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_subgrado} - {self.id_grado}"

    class Meta:
        verbose_name = 'T014GradoSubGrado'
        verbose_name_plural = 'T014GradoSubGrados'
        db_table = 'T014GradoSubGrado'




class TipoDocumento(models.Model):
    tipocodigo = models.CharField(max_length=10)
    nombre_codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_codigo

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'
        db_table = 'T015tipos_documento_id'


class Generos(models.Model):
    codigoGenero = models.CharField(max_length=10)
    nombre_Genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_Genero

    class Meta:
        verbose_name = 'Generos'
        verbose_name_plural = 'Generos'
        db_table = 'T019Genero'




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
    pertenece_universidad = models.BooleanField(default=False)
    universidad = models.ForeignKey(Universidad, on_delete=models.SET_NULL, null=True, blank=True)
    id_grado = models.ForeignKey(Grado, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        db_table = 'T005estudiantes_registrados'





class CategoriaLibros(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    otra_categoria_cual = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        verbose_name = 'Categoría de Libros'
        verbose_name_plural = 'Categorías de Libros'
        db_table = 'T004CategoriaLibros'



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
        db_table = 'T025Editoriales'

class Libro(models.Model):
    idISBN = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=200)
    categoriaLibro = models.ForeignKey(CategoriaLibros, on_delete=models.CASCADE)
    disponibleEnBiblioteca = models.BooleanField(default=True)
    Editorial = models.ForeignKey(Editorial, on_delete=models.SET_NULL, null=True, blank=True)
    id_Autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    agno_publicacion = models.PositiveIntegerField(null=True,blank=True)  # Año de publicación
    descripcion = models.TextField(null=True,blank=True)  # Descripción
    cantidad_copias = models.PositiveIntegerField(null=True,blank=True)  # Cantidad de copias
    cantidad_copiad_disponibles = models.PositiveIntegerField(null=True,blank=True)  # Cantidad de copias disponibles

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        db_table = 'T001Libros'



class EstadosCopiasLibros(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Estado de Copia de Libro'
        verbose_name_plural = 'Estados de Copias de Libros'
        db_table = 'T024Estados_Copias_Libros'


class CopiasLibros(models.Model):
    numero_registro = models.CharField(max_length=100)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    estado_copia = models.ForeignKey(EstadosCopiasLibros, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_registro

    class Meta:
        verbose_name = 'Copia de Libro'
        verbose_name_plural = 'Copias de Libros'
        db_table = 'T023CopiasLibros'


class Estantes(models.Model):
    # Llave primaria personalizada
    id_estante = models.CharField(max_length=100, primary_key=True)
    identificacion_estante = models.CharField(max_length=100,null=True,blank=True)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True)
    id_copia_libro = models.ForeignKey(CopiasLibros, on_delete=models.CASCADE, null=True)
    # Otros campos de tu modelo

    def __str__(self):
        return self.id_estante

    class Meta:
        verbose_name = 'Estante'
        verbose_name_plural = 'Estantes'
        db_table = 'T021Estantes'



class BandejaEntrante(models.Model):
    # Estableciendo una relación con el modelo Estantes
    estante = models.ForeignKey(Estantes, on_delete=models.CASCADE, null=True)
    identificacion_por_estante = models.CharField(max_length=100)
    orden_ubicacion_estante = models.IntegerField()
    # Otros campos de tu modelo

    def __str__(self):
        return self.identificacion_por_estante

    class Meta:
        verbose_name = 'Bandeja Entrante'
        verbose_name_plural = 'Bandejas Entrantes'
        db_table = 'T022Bandeja_Entrante'


class LibrosAutores(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Relación entre {self.libro} y {self.autor}"

    class Meta:
        verbose_name = 'Libros y Autores'
        verbose_name_plural = 'Libros y Autores'
        db_table = 'T003Libros_Autores'




from django.utils import timezone

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion_libro = models.DateField()
    tiempo_devolucion_dias = models.IntegerField()
    ya_devuelto = models.BooleanField()
    fecha_devolucion_real = models.TextField(default=str(timezone.now()))  # Valor por defecto utilizando timezone.now()
    observaciones_devolucion = models.TextField()
    dias_mora = models.TextField(default='')  # Valor por defecto como cadena vacía

    def __str__(self):
        return f"Prestamo de {self.libro} a {self.estudiante}"

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        db_table = 'T020Prestamos'


class Catalogos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad_libros_asociados = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Catálogo'
        verbose_name_plural = 'Catálogos'
        db_table = 'T027Catalogos'


class CatalogosLibros(models.Model):
    catalogo = models.ForeignKey(Catalogos, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Relación entre {self.catalogo} y {self.libro}"

    class Meta:
        verbose_name = 'Catálogo y Libro'
        verbose_name_plural = 'Catálogos y Libros'
        db_table = 'T028CatalogosLibros'



class ProgramaAcademicos(models.Model):
    codigo_programacion = models.CharField(max_length=10)
    nombre_programa = models.CharField(max_length=100)
    id_univercidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre_programa

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'
        db_table = 'T007Programas'



class EstudianteProgramaAcademicos(models.Model):
    
    id_estudainte = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    ubicacion_semestral = models.CharField(max_length=100)
    id_programa_academico = models.ForeignKey(ProgramaAcademicos, on_delete=models.CASCADE)
    def __str__(self):
        return self.ubicacion_semestral

    class Meta:
        verbose_name = 'Programa Academico'
        verbose_name_plural = 'Programas Academicos'
        db_table = 'T008Estudiante_Programas_Academico'


