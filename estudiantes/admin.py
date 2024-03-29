from django.contrib import admin
from .models import Estudiante, Colegio,Grado,Universidad,Jornada,GradosColegiosClavesForaneas,SubGrados,GradoSubGrado,TipoDocumento,Generos,BandejaEntrante,Estantes,CategoriaLibros,Libro,Autor,LibrosAutores,Prestamo,Editorial,EstadosCopiasLibros,CopiasLibros,Estantes,Catalogos,CatalogosLibros,ProgramaAcademicos,EstudianteProgramaAcademicos

# Registra los modelos uno por uno
admin.site.register(Estudiante)
admin.site.register(Colegio)
admin.site.register(Grado)
admin.site.register(Universidad)
admin.site.register(Jornada)
admin.site.register(GradosColegiosClavesForaneas)
admin.site.register(SubGrados)
admin.site.register(GradoSubGrado)
admin.site.register(TipoDocumento)
admin.site.register(Generos)
admin.site.register(BandejaEntrante)
admin.site.register(Estantes)
admin.site.register(CategoriaLibros)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(LibrosAutores)
admin.site.register(Prestamo)
admin.site.register(Editorial)
admin.site.register(EstadosCopiasLibros)
admin.site.register(CopiasLibros)
admin.site.register(Catalogos)
admin.site.register(CatalogosLibros)
admin.site.register(ProgramaAcademicos)
admin.site.register(EstudianteProgramaAcademicos)
