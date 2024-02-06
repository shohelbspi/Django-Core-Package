from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2','groups']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
