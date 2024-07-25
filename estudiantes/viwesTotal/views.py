from rest_framework import generics
from django.shortcuts import render
from estudiantes.models import TipoDocumento,Generos,Estantes,CategoriaLibros,Libro,Autor, Usuario
from estudiantes.serializers.estudiantes_serializers import TipoDocumentoerializer,LibroPostSerializer,GenerosSerializer,EstantesSerializer,CategoriaLibrosSerializer,LibroSerializer,AutorSerializer, Usuarioserializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError,NotFound,PermissionDenied



class CrearUsuario(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'detail': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ListarUsuario(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)




class BorrarUsuario(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

class ActualizarUsuario(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)



# crear vita para tipo Documento
class CrearTipoDocumentoVista(generics.CreateAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        

# class ListarTipoDocumentoVista(generics.ListAPIView):
#     queryset = TipoDocumento.objects.all()
#     serializer_class = TipoDocumentoerializer

#     def get(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({
#             'success': True,
#             'detail': 'Lista de personas registradas',
#             'data': serializer.data
#         }, status=status.HTTP_200_OK)
    
class ListarTipoDocumentoVista(generics.ListAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class ListarGeneroVista(generics.ListAPIView):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)



class BorrarTipoDocumentoVista(generics.DestroyAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

class ActualizarTipoDocumentoVista(generics.UpdateAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)






# crear vita para tipo Genero
class CrearGeneroVista(generics.CreateAPIView):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        

class BorrarGeneroVista(generics.DestroyAPIView):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

class ActualizarGeneroVista(generics.UpdateAPIView):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)





# crear vita para tipo BandejaEntrante
class CrearEstantesVista(generics.CreateAPIView):
    queryset = Estantes.objects.all()
    serializer_class = EstantesSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        
class ListarEstantesVista(generics.ListAPIView):
    queryset = Estantes.objects.all()
    serializer_class =EstantesSerializer


    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarEstantesVista(generics.DestroyAPIView):
    queryset = Estantes.objects.all()
    serializer_class = EstantesSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


class ActualizarEstantesVista(generics.UpdateAPIView):
    queryset = Estantes.objects.all()
    serializer_class = EstantesSerializer


    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    

    
# crear vita para tipo CategoriaLibrosSerializer
class CrearCategoriaLibrosVista(generics.CreateAPIView):
    queryset = CategoriaLibros.objects.all()
    serializer_class = CategoriaLibrosSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        
class ListarCategoriaLibrosVista(generics.ListAPIView):
    queryset = CategoriaLibros.objects.all()
    serializer_class =CategoriaLibrosSerializer


    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarCategoriaLibrosVista(generics.DestroyAPIView):
    queryset = CategoriaLibros.objects.all()
    serializer_class = CategoriaLibrosSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


class ActualizarCategoriaLibrosVista(generics.UpdateAPIView):
    queryset = CategoriaLibros.objects.all()
    serializer_class = CategoriaLibrosSerializer


    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    

# crear vita para tipo Libro
class CrearLibrosVista(generics.CreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroPostSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        

      
class ListarLibrosVista(generics.ListAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        queryset = Libro.objects.all()
        titulo = self.request.query_params.get('titulo', None)
        disponible = self.request.query_params.get('disponibleEnBiblioteca', None)
        editorial = self.request.query_params.get('Editorial', None)
        agno_publicacion = self.request.query_params.get('agno_publicacion', None)

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        if disponible is not None:
            queryset = queryset.filter(disponibleEnBiblioteca=disponible.lower() == 'true')
        if editorial:
            queryset = queryset.filter(Editorial__nombre__icontains=editorial)
        if agno_publicacion:
            queryset = queryset.filter(agno_publicacion=agno_publicacion)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de libros',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    
class BorrarLibrosVista(generics.DestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


class ActualizarLibrosVista(generics.UpdateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    



# crear vita para tipo Libro
class CrearAutorVista(generics.CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        
class ListarAutorVista(generics.ListAPIView):
    queryset = Autor.objects.all()
    serializer_class =AutorSerializer


    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarAutorVista(generics.DestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


class ActualizarAutorVista(generics.UpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    

