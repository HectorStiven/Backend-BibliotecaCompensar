from django.contrib import admin
from .models import Estudiante, Colegio,Grado,Jornada,TipoDocumento,Generos,Estantes,CategoriaLibros,Libro,Autor,Prestamo,Editorial,Estantes
# Registra los modelos uno por uno
admin.site.register(Estudiante)
admin.site.register(Colegio)
admin.site.register(Grado)
admin.site.register(Jornada)
admin.site.register(TipoDocumento)
admin.site.register(Generos)
admin.site.register(Estantes)
admin.site.register(CategoriaLibros)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Prestamo)
admin.site.register(Editorial)
