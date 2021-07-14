from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	class Meta:
		model= User
		fields = ('username','first_name', 'last_name','email', 'password1', 'password2')


class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50)
	email = forms.EmailField(max_length = 150)
	subject=forms.CharField(max_length=300)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)



