from django import forms
from .models import *

class ModeloForm(forms.ModelForm):
    class Meta:
        model= Modelo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            }) 



class ClientForm(forms.ModelForm):
    class Meta:
        model= category_client
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            }) 





class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields = "__all__"
        
    state = forms.ChoiceField(choices=((True, 'Activo'), (False, 'Inactivo')), widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            }) 




class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = "__all__"

    status_iva = forms.ChoiceField(choices=((True, 'Activo'), (False, 'Inactivo')), widget=forms.Select(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=((True, 'Activo'), (False, 'Inactivo')), widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            }) 
