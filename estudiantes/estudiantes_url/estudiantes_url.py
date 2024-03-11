from django.urls import path

from estudiantes.viwesTotal.viwes2 import ActualizarPersonaVista, BorrarPersonaVista, CrearPersonaVista, ListarPersonaVista,CrearColeguiVista,ListarColeguiVista,BorrarColegiVista,ActualizarColeguiVista,CrearGradosVista,ListarGradosVista,BorrarGradosVista,ActualizarGradosVista,ListarGradosVista
from estudiantes.viwesTotal.views import CrearCategoriaLibrosVista,ListarCategoriaLibrosVista,BorrarCategoriaLibrosVista,ActualizarCategoriaLibrosVista

urlpatterns = [
        path('crear_estudiante/', CrearPersonaVista.as_view(), name='crear_estudiante'),
        path('obtener_estudiante/', ListarPersonaVista.as_view(), name='obtener_estudiante'),
        path('borrar_estudiante/<int:pk>', BorrarPersonaVista.as_view(), name='borrar_estudiante'),
        path('actualizar_estudiante/<int:pk>', ActualizarPersonaVista.as_view(), name='actualizar_estudiante'),

        path('crear_coleguio/', CrearColeguiVista.as_view(), name='crear_coleguio'),
        path('obtener_coleguio/', ListarColeguiVista.as_view(), name='obtener_coleguio'),
        path('borrar_coleguio/<int:pk>', BorrarColegiVista.as_view(), name='borrar_coleguio'),
        path('actualizar_coleguio/<int:pk>', ActualizarColeguiVista.as_view(), name='actualizar_coleguio'),



        path('crear_Grados/', CrearGradosVista.as_view(), name='crear_Grados'),
        path('obtener_Grados/', ListarGradosVista.as_view(), name='obtener_Grados'),
        path('borrar_Grados/<int:pk>', BorrarGradosVista.as_view(), name='borrar_Grados'),
        path('actualizar_Grados/<int:pk>', ActualizarGradosVista.as_view(), name='actualizar_Grados'),


        path('crear_Categoria/', CrearCategoriaLibrosVista.as_view(), name='crear_Categoria'),
        path('obtener_Categoria/', ListarCategoriaLibrosVista.as_view(), name='obtener_Categoria'),
        path('borrar_Categoria/<int:pk>', BorrarCategoriaLibrosVista.as_view(), name='borrar_Categoria'),
        path('actualizar_Categoria/<int:pk>', ActualizarCategoriaLibrosVista.as_view(), name='actualizar_Categoria'),
        
]


