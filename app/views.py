from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.

#Funcion que se va a encargar de leer el Archivo Html que tenemos en la carpeta Template

class ModeloView(generic.ListView):
    permission_required = "app.view_modelo"
    model = Modelo
    template_name = "app/modelo_list.html"
    context_object_name = "obj"

class ModeloNew(generic.CreateView):
    permission_required="app.add_modelo"
    model=Modelo
    template_name="app/modelo_form.html"
    context_object_name = "obj"
    form_class=ModeloForm
    success_url=reverse_lazy("app:modelo_list")
    

class ModeloEdit(generic.UpdateView):
    permission_required="app.change_modelo"
    model=Modelo
    template_name="app/modelo_form.html"
    context_object_name = "obj"
    form_class=ModeloForm
    success_url=reverse_lazy("app:modelo_list")
    success_message="Modelo Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ModeloDel(generic.DeleteView):
    permission_required="app.delete_modelo"
    model=Modelo
    template_name='app/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("app:modelo_list")
    success_message="Modelo Eliminado Satisfactoriamente"




#------------------------------------------------Tabla Cliente-------------------------------------------------

class HtmlInicio(generic.TemplateView):
    template_name ="app/index.html"

class ClientView(generic.ListView):
    model = category_client
    template_name = "app/modelo_list.html"
    context_object_name = "obj"

class ClientNew(generic.CreateView):
    model=category_client
    template_name="app/modelo_form.html"
    context_object_name = "obj"
    form_class=ClientForm
    success_url=reverse_lazy("app:modelo_list")
    

class ClientEdit(generic.UpdateView):
    model=category_client
    template_name="app/modelo_form.html"
    context_object_name = "obj"
    form_class=ClientForm
    success_url=reverse_lazy("app:modelo_list")
    success_message="Modelo Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ClientDel(generic.DeleteView):
    model = category_client
    template_name = "app/modelo_form.html"  # Elige el nombre de tu plantilla de confirmación de eliminación
    context_object_name = 'obj'  # Nombre del objeto a eliminar, puedes cambiarlo si lo deseas
    success_url = reverse_lazy("app:modelo_list")  # URL a la que se redirigirá después de eliminar el objeto
    success_message = "Modelo eliminado satisfactoriamente"  # Mensaje de éxito que se mostrará




#------------------------------------------------Vistas Tabla Categoria-------------------------------------------------

class CategoryView(generic.ListView):
    model = Category
    template_name = "app/modelo_list.html"
    context_object_name = "obj"

class CategoryNew(generic.CreateView):
    model=Category
    template_name="app/modelo_form.html"
    context_object_name = "obj"
    form_class=CategoryForm
    success_url=reverse_lazy("app:modelo_list")
    

class CategoryEdit(generic.UpdateView):
    model=Category
    template_name="app/modelo_form.html"
    context_object_name = "obj"
    form_class=CategoryForm
    success_url=reverse_lazy("app:modelo_list")
    success_message="Modelo Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoryDel(generic.DeleteView):
    model = Category
    template_name = "app/modeloDel_form.html"  # Elige el nombre de tu plantilla de confirmación de eliminación
    context_object_name = 'obj'  # Nombre del objeto a eliminar, puedes cambiarlo si lo deseas
    success_url = reverse_lazy("app:modelo_list")  # URL a la que se redirigirá después de eliminar el objeto
    success_message = "Modelo eliminado satisfactoriamente"  # Mensaje de éxito que se mostrará


#------------------------------------------------Vistas Tabla Producto-------------------------------------------------

class ProductView(generic.ListView):
    model = Product
    template_name = "app/productos_list.html"
    context_object_name = "obj"

class ProductNew(generic.CreateView):
    model=Product
    template_name="app/productos_form.html"
    context_object_name = "obj"
    form_class=ProductForm
    success_url=reverse_lazy("app:productos_list")
    

class ProductEdit(generic.UpdateView):
    model=Product
    template_name="app/productos_form.html"
    context_object_name = "obj"
    form_class=ProductForm
    success_url=reverse_lazy("app:productos_list")
    success_message="Modelo Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ProductDel(generic.DeleteView):
    model = Product
    template_name = "app/productosDel.html"  # Elige el nombre de tu plantilla de confirmación de eliminación
    context_object_name = 'obj'  # Nombre del objeto a eliminar, puedes cambiarlo si lo deseas
    success_url = reverse_lazy("app:productos_list")  # URL a la que se redirigirá después de eliminar el objeto
    success_message = "Modelo eliminado satisfactoriamente"  # Mensaje de éxito que se mostrará

