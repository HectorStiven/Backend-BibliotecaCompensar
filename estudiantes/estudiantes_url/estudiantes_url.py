from django.urls import path
from estudiantes.viwesTotal import viwes2 as views2
from estudiantes.viwesTotal import views as views


urlpatterns = [
    # URLs para Estudiante
    path('crear_estudiante/', views2.CrearPersonaVista.as_view(), name='crear_estudiante'),
    path('obtener_estudiante/', views2.ListarPersonaVista.as_view(), name='obtener_estudiante'),
    path('borrar_estudiante/<int:pk>/', views2.BorrarPersonaVista.as_view(), name='borrar_estudiante'),
    path('actualizar_estudiante/<int:pk>/', views2.ActualizarPersonaVista.as_view(), name='actualizar_estudiante'),
    
    # URLs para Colegio
    path('crear_colegio/', views2.CrearColeguiVista.as_view(), name='crear_colegio'),
    path('obtener_colegio/', views2.ListarColeguiVista.as_view(), name='obtener_colegio'),
    path('borrar_colegio/<int:pk>/', views2.BorrarColegiVista.as_view(), name='borrar_colegio'),
    path('actualizar_colegio/<int:pk>/', views2.ActualizarColeguiVista.as_view(), name='actualizar_colegio'),

    # URLs para Grado
    path('crear_grado/', views2.CrearGradosVista.as_view(), name='crear_grado'),
    path('obtener_grado/', views2.ListarGradosVista.as_view(), name='obtener_grado'),
    path('borrar_grado/<int:pk>/', views2.BorrarGradosVista.as_view(), name='borrar_grado'),
    path('actualizar_grado/<int:pk>/', views2.ActualizarGradosVista.as_view(), name='actualizar_grado'),

    # URLs para Jornada
    path('crear_jornada/', views2.CrearJornadaVista.as_view(), name='crear_jornada'),
    path('obtener_jornada/', views2.ListarJornadaVista.as_view(), name='obtener_jornada'),
    path('borrar_jornada/<int:pk>/', views2.BorrarJornadaVista.as_view(), name='borrar_jornada'),
    path('actualizar_jornada/<int:pk>/', views2.ActualizarJornadaVista.as_view(), name='actualizar_jornada'),

    # URLs para Prestamo
    path('crear_prestamo/', views2.CrearPrestamoVista.as_view(), name='crear_prestamo'),
    path('obtener_prestamo/', views2.ListarPrestamoVista.as_view(), name='obtener_prestamo'),
    path('borrar_prestamo/<int:pk>/', views2.BorrarPrestamoVista.as_view(), name='borrar_prestamo'),
    path('actualizar_prestamo/<int:pk>/', views2.ActualizarPrestamoVista.as_view(), name='actualizar_prestamo'),

    # URLs para Editorial
    path('crear_editorial/', views2.CrearEditorialVista.as_view(), name='crear_editorial'),
    path('obtener_editorial/', views2.ListarEditorialVista.as_view(), name='obtener_editorial'),
    path('borrar_editorial/<int:pk>/', views2.BorrarEditorialVista.as_view(), name='borrar_editorial'),
    path('actualizar_editorial/<int:pk>/', views2.ActualizarEditorialVista.as_view(), name='actualizar_editorial'),
    

    # URLs para Usuario
    path('crear_usuario/', views.Cre
         arUsuario.as_view(), name='crear_usuario'),
    path('listar_usuario/', views.ListarUsuario.as_view(), name='listar_usuario'),
    path('borrar_usuario/<int:pk>/', views.BorrarUsuario.as_view(), name='borrar_usuario'),
    path('actualizar_usuario/<int:pk>/', views.ActualizarUsuario.as_view(), name='actualizar_usuario'),

    # URLs para TipoDocumento
    path('crear_tipo_documento/', views.CrearTipoDocumentoVista.as_view(), name='crear_tipo_documento'),
    path('listar_tipo_documento/', views.ListarTipoDocumentoVista.as_view(), name='listar_tipo_documento'),
    path('borrar_tipo_documento/<int:pk>/', views.BorrarTipoDocumentoVista.as_view(), name='borrar_tipo_documento'),
    path('actualizar_tipo_documento/<int:pk>/', views.ActualizarTipoDocumentoVista.as_view(), name='actualizar_tipo_documento'),

    # URLs para Genero
    path('crear_genero/', views.CrearGeneroVista.as_view(), name='crear_genero'),
    path('listar_genero/', views.ListarGeneroVista.as_view(), name='listar_genero'),
    path('borrar_genero/<int:pk>/', views.BorrarGeneroVista.as_view(), name='borrar_genero'),
    path('actualizar_genero/<int:pk>/', views.ActualizarGeneroVista.as_view(), name='actualizar_genero'),

    # URLs para Estantes
    path('crear_estantes/', views.CrearEstantesVista.as_view(), name='crear_estantes'),
    path('listar_estantes/', views.ListarEstantesVista.as_view(), name='listar_estantes'),
    path('borrar_estantes/<int:pk>/', views.BorrarEstantesVista.as_view(), name='borrar_estantes'),
    path('actualizar_estantes/<int:pk>/', views.ActualizarEstantesVista.as_view(), name='actualizar_estantes'),

    # URLs para CategoriaLibros
    path('crear_categoria_libros/', views.CrearCategoriaLibrosVista.as_view(), name='crear_categoria_libros'),
    path('listar_categoria_libros/', views.ListarCategoriaLibrosVista.as_view(), name='listar_categoria_libros'),
    path('borrar_categoria_libros/<int:pk>/', views.BorrarCategoriaLibrosVista.as_view(), name='borrar_categoria_libros'),
    path('actualizar_categoria_libros/<int:pk>/', views.ActualizarCategoriaLibrosVista.as_view(), name='actualizar_categoria_libros'),

    # URLs para Libros
    path('crear_libros/', views.CrearLibrosVista.as_view(), name='crear_libros'),
    path('listar_libros/', views.ListarLibrosVista.as_view(), name='listar_libros'),
    path('borrar_libros/<int:pk>/', views.BorrarLibrosVista.as_view(), name='borrar_libros'),
    path('actualizar_libros/<int:pk>/', views.ActualizarLibrosVista.as_view(), name='actualizar_libros'),

    # URLs para Autor
    path('crear_autor/', views.CrearAutorVista.as_view(), name='crear_autor'),
    path('listar_autor/', views.ListarAutorVista.as_view(), name='listar_autor'),
    path('borrar_autor/<int:pk>/', views.BorrarAutorVista.as_view(), name='borrar_autor'),
    path('actualizar_autor/<int:pk>/', views.ActualizarAutorVista.as_view(), name='actualizar_autor'),


]
