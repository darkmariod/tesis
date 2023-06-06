from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	codigo_institucion_externa = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Código Institución Externa", "class":"form-control"}), label="")
	codigo_senecyt = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Código Senecyt", "class":"form-control"}), label="")
	codigo_toma_fisica = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Código Toma Física", "class":"form-control"}), label="")
	codigo_anterior = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Código Senecyt", "class":"form-control"}), label="")
	bien = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Bien", "class":"form-control"}), label="")
	clase_bien = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Clase Bien", "class":"form-control"}), label="")
	serie = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Serie", "class":"form-control"}), label="")
	modelo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Modelo", "class":"form-control"}), label="")
	color = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Color", "class":"form-control"}), label="")
	material = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Material", "class":"form-control"}), label="")
	marca = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Marca", "class":"form-control"}), label="")
	estado = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Estado", "class":"form-control"}), label="")
	usuario_final = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Usuario Final", "class":"form-control"}), label="")
	nro_cedula = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nro Cédula", "class":"form-control"}), label="")
	ubicacion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ubicación", "class":"form-control"}), label="")
	edificio = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Edificio", "class":"form-control"}), label="")
	custodio_administrativo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Custodio Administrativo", "class":"form-control"}), label="")
	delegado_1 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Delegado 1", "class":"form-control"}), label="")
	delegado_2 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Delegado 2", "class":"form-control"}), label="")
	delegado_3 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Delegado 3", "class":"form-control"}), label="")
	tipo_novedad = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tipo de Novedad", "class":"form-control"}), label="")
	observaciones = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Observaciones", "class":"form-control"}), label="")
	nro_acta_entrega_recepcion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nro Acta Recepción", "class":"form-control"}), label="")
	nro_acta_donacion_factura = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nro Acta Donación", "class":"form-control"}), label="")
	valor_monetario = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Valor Monetario", "class":"form-control"}), label="")
	fecha_entrega_recepcion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Fecha Entrega Recepción", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)