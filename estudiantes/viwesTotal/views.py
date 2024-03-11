from rest_framework import generics
from django.shortcuts import render
from estudiantes.models import GradosColegiosClavesForaneas,SubGrados,GradoSubGrado,TipoDocumento,Generos,BandejaEntrante,Estantes,CategoriaLibros,Libro,Autor
from estudiantes.serializers.estudiantes_serializers import GradosColegiosSerializer,SubGradoserializer,GradoSubGradoserializer,TipoDocumentoerializer,GenerosSerializer,BandejaEntranteSerializer,EstantesSerializer,CategoriaLibrosSerializer,LibroSerializer,AutorSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError,NotFound,PermissionDenied





# crear vita para Gradoscolegios
class CrearGradoColegioVista(generics.CreateAPIView):
    queryset = GradosColegiosClavesForaneas.objects.all()
    serializer_class = GradosColegiosSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        
        
class ListarGradoColegioVista(generics.ListAPIView):
    queryset = GradosColegiosClavesForaneas.objects.all()
    serializer_class = GradosColegiosSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarGradoColegioVista(generics.DestroyAPIView):
    queryset = GradosColegiosClavesForaneas.objects.all()
    serializer_class = GradosColegiosSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActualizarGradoColegioVista(generics.UpdateAPIView):
    queryset = GradosColegiosClavesForaneas.objects.all()
    serializer_class = GradosColegiosSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    





# crear vita para Gradoscolegios

class CrearSubGradooVista(generics.CreateAPIView):
    queryset = SubGrados.objects.all()
    serializer_class = SubGradoserializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        
        
class ListarSubGradooVista(generics.ListAPIView):
    queryset = SubGrados.objects.all()
    serializer_class = SubGradoserializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarSubGradooVista(generics.DestroyAPIView):
    queryset = SubGrados.objects.all()
    serializer_class = SubGradoserializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActualizarSubGradooVista(generics.UpdateAPIView):
    queryset = SubGrados.objects.all()
    serializer_class = SubGradoserializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    



# crear vita para Gradoscolegios
class CrearGradoSubGradoVista(generics.CreateAPIView):
    queryset = GradoSubGrado.objects.all()
    serializer_class = GradoSubGradoserializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        
class ListarGradoSubGradoVista(generics.ListAPIView):
    queryset = GradoSubGrado.objects.all()
    serializer_class = GradoSubGradoserializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarGradoSubGradoVista(generics.DestroyAPIView):
    queryset = GradoSubGrado.objects.all()
    serializer_class = GradoSubGradoserializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActualizarGradoSubGradoVista(generics.UpdateAPIView):
    queryset = GradoSubGrado.objects.all()
    serializer_class = GradoSubGradoserializer

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

class BorrarTipoDocumentoVista(generics.DestroyAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

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

class BorrarGeneroVista(generics.DestroyAPIView):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

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
class CrearBandejaEntranteVista(generics.CreateAPIView):
    queryset = BandejaEntrante.objects.all()
    serializer_class = BandejaEntranteSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        
class ListarBandejaEntranteVista(generics.ListAPIView):
    queryset = BandejaEntrante.objects.all()
    serializer_class = BandejaEntranteSerializer


    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarBandejaEntranteVista(generics.DestroyAPIView):
    queryset = BandejaEntrante.objects.all()
    serializer_class = BandejaEntranteSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActualizarBandejaEntranteVista(generics.UpdateAPIView):
    queryset = BandejaEntrante.objects.all()
    serializer_class = BandejaEntranteSerializer


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
        return Response(status=status.HTTP_204_NO_CONTENT)


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
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    serializer_class = LibroSerializer

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
    queryset = Libro.objects.all()
    serializer_class =LibroSerializer


    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarLibrosVista(generics.DestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActualizarAutorVista(generics.UpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    

