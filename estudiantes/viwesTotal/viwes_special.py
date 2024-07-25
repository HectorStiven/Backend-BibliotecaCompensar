from estudiantes.models import Prestamo
from rest_framework.response import Response
from rest_framework import generics
from datetime import date
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.exceptions import ValidationError,NotFound,PermissionDenied




class ActualizarTodosPrestamosView(generics.UpdateAPIView):
    def get(self, request, *args, **kwargs):
        prestamos = Prestamo.objects.all()
        actualizados = 0

        for prestamo in prestamos:
            dias_mora = self.calcular_dias_mora(prestamo)
            if prestamo.dias_mora != dias_mora:
                prestamo.dias_mora = dias_mora
                prestamo.save()
                actualizados += 1

        return Response({'mensaje': f'Se actualizaron {actualizados} préstamos correctamente.'}, status=200)

    def calcular_dias_mora(self, prestamo):
        # Verifica si el libro no ha sido devuelto
        if not prestamo.ya_devuelto:
            # Verifica si hay una fecha de préstamo válida
            if prestamo.fecha_prestamo:
                # Calcula los días desde la fecha de préstamo hasta la fecha actual
                dias_prestamo = (date.today() - prestamo.fecha_prestamo).days
                # Calcula los días de mora restando los días permitidos
                dias_mora = dias_prestamo - prestamo.tiempo_devolucion_dias
                # Retorna los días de mora si es mayor a 0, de lo contrario retorna 0
                return max(dias_mora, 0)
        # Retorna 0 si el libro ya ha sido devuelto o no hay fecha de préstamo
        return 0










class EnviarCorreoElectronico(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        correo = request.data.get('correo')
        nombre = request.data.get('nombre')
        subject = request.data.get('asunto')
        mensaje = request.data.get('mensaje')

        if correo and nombre and subject:
            # Configuración del correo electrónico
            template = "alerta.html"
            
            # Crear el contexto para la plantilla
            context = {
                'nombre': nombre,
                'mensaje': mensaje
            }

            # Renderizar la plantilla
            html_content = render_to_string(template, context)

            # Configuración del correo electrónico en formato HTML
            email = EmailMessage()
            email.subject = subject
            email.body = html_content
            email.to = [correo]
            email.content_subtype = 'html'

            try:
                # Enviar el correo electrónico
                email.fail_silently=False
                email.send()
                return Response({'mensaje': 'Correo electrónico enviado correctamente'}, status=status.HTTP_200_OK)
            except Exception as e:
                # Maneja cualquier error al enviar el correo
                return Response({'error': f'Error al enviar el correo: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # Maneja el caso en el que no se proporciona el correo, el nombre o el asunto
            return Response({'error': 'Por favor, proporciona el correo, el nombre y el asunto.'}, status=status.HTTP_400_BAD_REQUEST)