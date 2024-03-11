from rest_framework import serializers
from estudiantes.models import Estudiante,Colegio,Grado,Universidad,GradosColegiosClavesForaneas,Jornada,SubGrados,GradoSubGrado,TipoDocumento,Generos,BandejaEntrante,Estantes,CategoriaLibros,Libro,Autor,LibrosAutores,Prestamo,Editorial,EstadosCopiasLibros,CopiasLibros,Catalogos,CatalogosLibros,ProgramaAcademicos,EstudianteProgramaAcademicos

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class ColeguioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colegio
        fields = '__all__'

class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields = '__all__'


class UnivercidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = '__all__'


class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = '__all__'

class GradosColegiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradosColegiosClavesForaneas
        fields = '__all__'

class SubGradoserializer(serializers.ModelSerializer):
    class Meta:
        model = SubGrados
        fields = '__all__'


class GradoSubGradoserializer(serializers.ModelSerializer):
    class Meta:
        model = GradoSubGrado
        fields = '__all__'

class TipoDocumentoerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'



class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'


class BandejaEntranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandejaEntrante
        fields = '__all__'




class EstantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estantes
        fields = '__all__'


class CategoriaLibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaLibros
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibrosAutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrosAutores
        fields = '__all__'



class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


class EstadosCopiasLibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadosCopiasLibros
        fields = '__all__'

class CopiasLibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopiasLibros
        fields = '__all__'

class CopiasLibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopiasLibros
        fields = '__all__'

class CatalogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogos
        fields = '__all__'

class CatalogosLibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogosLibros
        fields = '__all__'

class ProgramaAcademicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaAcademicos
        fields = '__all__'

class EstudianteProgramaAcademicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudianteProgramaAcademicos
        fields = '__all__'
