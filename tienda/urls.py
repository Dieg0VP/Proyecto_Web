from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),

    path('login/',views.login, name='login'),
    
    path('registro/',views.registro, name='registro'),
    
    path('catalogo/', views.catalogo_general, name='catalogo_general'),

    
    path('catalogo_desc/<int:catalogo_id>/', views.catalogo_desc, name='catalogo_desc'),

    
    path('contacto/',views.contacto, name='contacto'),

    path('agregar-producto/',views.agregar_producto, name='agregar-producto'),

    path('listar-producto/',views.listar_producto, name='listar-producto'),

    path('modificar-producto/<id>',views.modificar_producto, name='modificar-producto'),
    
    path('eliminar-producto/<id>',views.eliminar_producto, name='eliminar-producto'),

    path('salir/',views.salir, name='salir'),
]   