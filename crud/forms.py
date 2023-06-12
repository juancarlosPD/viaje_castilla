from locale import normalize
from django import forms
from django.forms import ModelForm
from crud.models import Pacientes, Patologias, Farmacos
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class PacientesForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nuhsa', 'nombre', 'apellido1', 'apellido2', 'fecha_nac', 'descripcion', 'patologia', 'riesgo_vascular', 'farmaco']
        widgets = {
            'nuhsa' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'NUHSA (imprescindible)',
                    
                    
                }
            ),
            'nombre' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'apellido1' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Primer apellido'
                }
            ),
            'apellido2' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Segundo apellido'
                }
            ),
            'descripcion' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Información de interés',
                    'rows':'3'         
                }
            ),
            'fecha_nac' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'aaaa-mm-dd'
                }
            ),
            'patologia' : forms.SelectMultiple(
                attrs={
                    'class' : 'form-control',
                    
                }
            ),
            'farmaco' : forms.SelectMultiple(
                attrs={
                    'class' : 'form-control',
                    
                }
            ),
            'riesgo_vascular' : forms.SelectMultiple(
                attrs={
                    'class' : 'form-control',
                    
                }
            )
        }

    def clean(self):
        # En la variable cleande recogemos los datos del formulario
        cleaned = super().clean()
        # Luego aplicamos una validación
        if len(cleaned['nuhsa']) <=8:
            self.add_error('nuhsa', 'Le faltan caracteres en el NUHSA')

        
        return cleaned

class PatologiasForm(forms.ModelForm):
    class Meta:
        model = Patologias
        fields = ['patologia','codigo']
        label = {
            'patologia' : 'Patología',
            'codigo' : 'CIE-9'
        }
        widgets = {
            'patologia' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Patologia'
                }
            ),'codigo' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'CIE-9'
                }
            )},

# class AuthenticationForm(forms.Form):
#     username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True}))
#     password = forms.CharField(
#         label=("Password"),
#         strip = False,
#         widget=forms.PasswordInput(attrs={'autocomplete':'current-password'}),
#     )

#     error_messages = {
#         'invalid_login': _(
#             "Por favvor introduzca un "
#         ),
#     }