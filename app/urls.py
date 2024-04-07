#Aqui van las URLS que estan relacionadas con las vistas
from django.urls import path #Para definir rutas
from .views import *

urlpatterns = [
    path('',HtmlInicio.as_view(),name="index"),   
    path('list',CategoryView.as_view(),name="modelo_list"),   
    path('new',CategoryNew.as_view(),name="new"),
    path('edit/<int:pk>',CategoryEdit.as_view(),name="edit"), 
    path('del/<int:pk>',CategoryDel.as_view(),name="del"), 

    path('listProducto',ProductView.as_view(),name="productos_list"),   
    path('newProducto',ProductNew.as_view(),name="newProducto"),
    path('editProducto/<int:pk>',ProductEdit.as_view(),name="editProducto"), 
    path('delProducto/<int:pk>',ProductDel.as_view(),name="delProducto"), 
]

