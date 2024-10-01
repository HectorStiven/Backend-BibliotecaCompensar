from rest_framework import generics
from estudiantes.models import  Usuario
from estudiantes.serializers.estudiantes_serializers import Usuarioserializer,AuthSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated




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
    permission_classes = [IsAuthenticated]
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


from django.contrib.auth.hashers import make_password, is_password_usable
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.permissions import AllowAny

class AutenticacionUsuario(generics.GenericAPIView):
    queryset = Usuario.objects.all()
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Validar datos del serializer
        if not serializer.is_valid():
            print("Errores de validación:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        numero_documento = serializer.validated_data['numeroDocumento']
        contrasena = serializer.validated_data['crearContrasena']

        print(f"Intentando autenticar usuario: {numero_documento}")

        try:
            # Buscar el usuario
            usuario = Usuario.objects.get(numeroDocumento=numero_documento)
            print(f"Usuario encontrado: {usuario}")

            # Verificar la contraseña usando un método personalizado
            if self.verify_password(contrasena, usuario.crearContrasena):
                print("Contraseña correcta.")

                # Generar tokens
                access_token = AccessToken.for_user(usuario)
                refresh_token = RefreshToken.for_user(usuario)

                usuario_data = {
                    'id': usuario.id,
                    'numeroDocumento': usuario.numeroDocumento,
                    # Agrega más campos según sea necesario
                }

                print(f"Token de acceso generado: {str(access_token)}")
                print(f"Token de actualización generado: {str(refresh_token)}")

                return Response({
                    'success': True,
                    'token': str(access_token),
                    'refresh': str(refresh_token),
                    'data': usuario_data,
                }, status=status.HTTP_200_OK)
            else:
                print("Contraseña incorrecta.")
                return Response({'success': False, 'detail': 'Contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

        except Usuario.DoesNotExist:
            print("Usuario no encontrado.")
            return Response({'success': False, 'detail': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        except Usuario.MultipleObjectsReturned:
            print("Múltiples usuarios encontrados.")
            return Response({'success': False, 'detail': 'Múltiples usuarios encontrados con el mismo número de documento'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")
            return Response({'success': False, 'detail': 'Ocurrió un error en el servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def verify_password(self, provided_password, stored_password):
        # Método simple para verificar la contraseña
        # Este es solo un ejemplo. Asegúrate de usar un método seguro para tu aplicación.
        return provided_password == stored_password