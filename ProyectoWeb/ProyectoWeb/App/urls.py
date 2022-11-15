from django.urls import path
from App import views

urlpatterns = [
    path("inicio", views.home, name="web-inicio"),
    path("masinformacion", views.info_personal, name="web-masinformarcion"),
    path("biblioteca", views.buscar_tracks, name="web-biblioteca"),
    path("biblioteca/busqueda", views.resultados_busqueda_canciones, name="web-biblioteca-resultado"),
    path("toolz", views.creacion_usuario, name="web-toolz"),
    path("toolz/inicio", views.programa_de_clases, name="web-toolz-inicio"),
    path("toolz/inicio/busqueda", views.resultado_busqueda_programa, name="web-toolz-busqueda"),
]