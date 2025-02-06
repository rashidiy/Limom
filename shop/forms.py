from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered with another account.')
        return email

from django import forms
from django.contrib.auth.models import User

class UserChangeForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
    username = forms.CharField(required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Username already taken')
        return username

    def clean_email(self):
        if self.instance:
            return self.instance.email
        return self.cleaned_data.get('email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
