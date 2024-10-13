from rest_framework import generics
from estudiantes.models import  Usuario
from estudiantes.serializers.estudiantes_serializers import Usuarioserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # Importar la clase de permisos




from django.contrib.auth.hashers import make_password, check_password


from rest_framework.permissions import AllowAny  # Importar la clase de permisos


# Crear Usuario
# class CrearUsuario(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = Usuarioserializer

#     def perform_create(self, serializer):
#         # Hasheando la contraseña antes de guardar el usuario
#         contrasena = serializer.validated_data.get('contrasena')
#         hashed_password = make_password(contrasena)
#         serializer.save(contrasena=hashed_password)

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)
#             return Response({
#                 'success': True,
#                 'detail': 'Usuario creado correctamente',
#                 'data': serializer.data
#             }, status=status.HTTP_201_CREATED)
#         return Response({
#             'success': False,
#             'detail': 'Error al crear el usuario',
#             'data': serializer.errors
#         }, status=status.HTTP_400_BAD_REQUEST)


class CrearUsuario(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserializer
    permission_classes = [AllowAny]  # Permitir a cualquier usuario crear una cuenta

    def perform_create(self, serializer):
        contrasena = serializer.validated_data.get('contrasena')
        if contrasena:
            # Hashear la contraseña
            serializer.validated_data['contrasena'] = make_password(contrasena)  
        serializer.save()

    def post(self, request, *args, **kwargs):
        # Crea un serializer con los datos de la solicitud
        serializer = self.get_serializer(data=request.data)

        # Verificar si el correo electrónico o número de identificación ya existen
        if Usuario.objects.filter(correo_electronico=request.data.get('correo_electronico')).exists():
            return Response({
                'success': False,
                'detail':'El correo electrónico ya está en uso.',
            }, status=status.HTTP_400_BAD_REQUEST)

        if Usuario.objects.filter(numeroDocumento=request.data.get('numeroDocumento')).exists():
            return Response({
                'success': False,
                'detail': 'El número de identificación ya está en uso.',
            }, status=status.HTTP_400_BAD_REQUEST)

        # Validar el serializer
        serializer.is_valid(raise_exception=True)

        # Almacena el usuario en la base de datos
        self.perform_create(serializer)  

        return Response({
            'success': True,
            'detail': 'Usuario creado exitosamente.',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


class ListarUsuario(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserializer
    permission_classes = [IsAuthenticated]  # Asegúrate de que se requiera autenticación

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


from django.contrib.auth.hashers import make_password, is_password_usable
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class AutenticacionUsuario(generics.GenericAPIView):
    serializer_class = Usuarioserializer

    def post(self, request, *args, **kwargs):
        numeroDocumento = request.data.get('numero_identificacion')
        contrasena = request.data.get('contrasena')

        # Validar campos vacíos
        if not numeroDocumento or not contrasena:
            return Response({
                'success': False,
                'detail': 'Número de identificación y contraseña son requeridos.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Buscar usuario por número de identificación
        try:
            usuario = Usuario.objects.get(numeroDocumento=numeroDocumento)
        except Usuario.DoesNotExist:
            return Response({
                'success': False,
                'detail': 'Usuario no encontrado.'
            }, status=status.HTTP_404_NOT_FOUND)

        # Comparar contraseñas usando check_password
        if check_password(contrasena, usuario.contrasena):  # Asegúrate de que este campo es el correcto para la contraseña
            # Generar tokens JWT
            refresh = RefreshToken.for_user(usuario)
            access_token = refresh.access_token

            return Response({
                'detail': 'Login exitoso.',
                'token': str(access_token),
                'data': Usuarioserializer(usuario).data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'detail': 'Contraseña incorrecta.'
            }, status=status.HTTP_400_BAD_REQUEST)