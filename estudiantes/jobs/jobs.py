from estudiantes.viwesTotal.viwes_special import ActualizarTodosPrestamosView
from rest_framework.test import APIRequestFactory
from rest_framework.response import Response


def generar_alerta():
    #Crear una solicitud simulada
    factory = APIRequestFactory()
    request = factory.get('/actualizar-todos-prestamos/')  # Ruta de la vista
    
    # Crear una instancia de la vista
    view = ActualizarTodosPrestamosView.as_view()

    # Llamar al método de la vista con la solicitud simulada
    response = view(request)

    # Procesar la respuesta de la vista
    if isinstance(response, Response):
        print(response.data)  # Imprime la respuesta de la vista
    else:
        print("Error: La vista no devolvió una respuesta válida.")
    
    print('TAREA realizada con éxito')
