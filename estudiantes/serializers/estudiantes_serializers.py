from rest_framework import serializers
from estudiantes.models import Estudiante,Colegio,Grado,Jornada,TipoDocumento,Generos,Estantes,CategoriaLibros,Libro,Autor,Prestamo,Editorial, Usuario

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



class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = '__all__'


class Usuarioserializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TipoDocumentoerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'



class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
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
    categoriaLibro = serializers.SlugRelatedField(slug_field='nombre_categoria', queryset=CategoriaLibros.objects.all())
    Editorial = serializers.SlugRelatedField(slug_field='nombre', queryset=Editorial.objects.all())
    id_Autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    id_estante = serializers.SlugRelatedField(slug_field='id_estante', queryset=Estantes.objects.all())

    class Meta:
        model = Libro
        fields = ['idISBN', 'titulo', 'disponibleEnBiblioteca', 'agno_publicacion', 'descripcion', 'estado_libro', 'cantidad_copias', 'categoriaLibro', 'Editorial', 'id_Autor', 'id_estante']

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


