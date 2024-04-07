from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .views import *

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('api/docs/', schema_view),
    path('', HtmlInicio.as_view(), name="index"),   
    path('list/', CategoryView.as_view(), name="modelo_list"),   
    path('new/', CategoryNew.as_view(), name="new"),
    path('edit/<int:pk>/', CategoryEdit.as_view(), name="edit"), 
    path('del/<int:pk>/', CategoryDel.as_view(), name="del"), 

    path('listProducto/', ProductView.as_view(), name="productos_list"),   
    path('newProducto/', ProductNew.as_view(), name="newProducto"),
    path('editProducto/<int:pk>/', ProductEdit.as_view(), name="editProducto"), 
    path('delProducto/<int:pk>/', ProductDel.as_view(), name="delProducto"),

    path('api/productos/', ProductoListView.as_view(), name='producto-list'),
]
