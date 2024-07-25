from rest_framework import generics
from django.shortcuts import render
from estudiantes.models import Estudiante,Grado,Colegio,Jornada,Prestamo,Editorial
from estudiantes.serializers.estudiantes_serializers import EstudianteSerializer,ColeguioSerializer,GradoSerializer,JornadaSerializer,PrestamoSerializer,EditorialSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from django.utils import timezone


# Create your views here.
class CrearPersonaVista(generics.CreateAPIView):
    permission_classes=[permissions.AllowAny]

    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
        
        
class ListarPersonaVista(generics.ListAPIView):
    serializer_class = EstudianteSerializer

    def get_queryset(self):
        # Obtener parámetros de consulta
        numero_identidad = self.request.query_params.get('numero_identidad', None)
        primer_nombre = self.request.query_params.get('primer_nombre', None)
        segundo_nombre = self.request.query_params.get('segundo_nombre', None)
        primer_apellido = self.request.query_params.get('primer_apellido', None)
        segundo_apellido = self.request.query_params.get('segundo_apellido', None)
        edad = self.request.query_params.get('edad', None)
        tipo_genero = self.request.query_params.get('tipo_genero', None)

        # Inicializar el queryset
        queryset = Estudiante.objects.all()

        # Aplicar filtros
        if numero_identidad:
            queryset = queryset.filter(numero_identidad__icontains=numero_identidad)
        if primer_nombre:
            queryset = queryset.filter(primer_nombre__icontains=primer_nombre)
        if segundo_nombre:
            queryset = queryset.filter(segundo_nombre__icontains=segundo_nombre)
        if primer_apellido:
            queryset = queryset.filter(primer_apellido__icontains=primer_apellido)
        if segundo_apellido:
            queryset = queryset.filter(segundo_apellido__icontains=segundo_apellido)
        if edad:
            queryset = queryset.filter(edad=edad)
        if tipo_genero:
            queryset = queryset.filter(tipo_genero=tipo_genero)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    



class BorrarPersonaVista(generics.DestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActualizarPersonaVista(generics.UpdateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', True))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    


 # crear vita para coleguioss.
class CrearColeguiVista(generics.CreateAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColeguioSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListarColeguiVista(generics.ListAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColeguioSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarColegiVista(generics.DestroyAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColeguioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActualizarColeguiVista(generics.UpdateAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColeguioSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    



# crear vita para Grados.
class CrearGradosVista(generics.CreateAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListarGradosVista(generics.ListAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de Grados registradss',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    
class BorrarGradosVista(generics.DestroyAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActualizarGradosVista(generics.UpdateAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    


class CrearJornadaVista(generics.CreateAPIView):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
            
class ListarJornadaVista(generics.ListAPIView):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarJornadaVista(generics.DestroyAPIView):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActualizarJornadaVista(generics.UpdateAPIView):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    






class CrearPrestamoVista(generics.CreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            # Guardar el préstamo
            prestamo = serializer.save()

            # Actualizar la cantidad de copias del libro
            libro = prestamo.libro
            if libro.cantidad_copias > 0:
                libro.cantidad_copias -= 1
                libro.save()
            else:
                return Response({'success': False, 'detail': 'No hay suficientes copias del libro disponibles'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'success': True, 'detail': 'Préstamo registrado correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'success': False, 'detail': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'success': False, 'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        





class DevolverLibroVista(generics.CreateAPIView):
    def post(self, request, prestamo_id, *args, **kwargs):
        try:
            # Buscar el préstamo por ID
            prestamo = Prestamo.objects.get(id=prestamo_id)

            # Validar si el libro ya ha sido devuelto
            if prestamo.ya_devuelto:
                return Response({'success': False, 'detail': 'El libro ya ha sido devuelto'}, status=status.HTTP_400_BAD_REQUEST)

            # Obtener el libro asociado al préstamo
            libro = prestamo.libro

            # Incrementar la cantidad de copias del libro
            libro.cantidad_copias += 1
            libro.save()

            # Actualizar el campo fecha_devolucion_real con la fecha y hora actuales
            prestamo.fecha_devolucion_real = timezone.now()
            prestamo.ya_devuelto = True
            prestamo.save()

            return Response({'success': True, 'detail': 'Libro devuelto con éxito'}, status=status.HTTP_200_OK)
        except Prestamo.DoesNotExist:
            return Response({'success': False, 'detail': 'Préstamo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({'success': False, 'detail': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'success': False, 'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class ListarPrestamoVista(generics.ListAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarPrestamoVista(generics.DestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActualizarPrestamoVista(generics.UpdateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    





# Create grados Editorial

class CrearEditorialVista(generics.CreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success':True,'detail':'persona registrada correctamente','data':serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError  as e:
            # error_message = {'error': e.detail}
            raise ValidationError(e.detail)
            
class ListarEditorialVista(generics.ListAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class BorrarEditorialVista(generics.DestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActualizarEditorialVista(generics.UpdateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados

        return Response(serializer.data, status=status.HTTP_200_OK)
    


