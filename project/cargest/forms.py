from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Car
from django.utils.translation import gettext_lazy as _  

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField(
        label=_("Edad"),
        required=True,
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario: ',
            'email': 'Email: ',
            'password1': 'Contraseña: ',
            'password2': 'Repita su contraseña: ',
        }
        help_texts = {
            'username': 'Requerido. Debe tener 150 caracteres o menos. Letras, dígitos y @.+-_ nada más. ',
            'password1': 'Su contraseña no puede ser igual a su información personal. Debe contener al menos ocho caracteres. Debe ser poco común y no puede ser enteramente numérica.',
            'password2': 'Ponga la contraseña anterior para',
        }

class CarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ['name', 'price', 'description', 'latitude', 'longitude']
        labels = {
            'name':'Nombre', 
            'price':'Precio',
            'description':'Descripción',
        }
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitude'].required = True
        self.fields['longitude'].required = True