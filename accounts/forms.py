# Django packages
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Third party apps
from phonenumber_field.formfields import PhoneNumberField
# Local apps
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'phone')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password2'] != cd['password1']:
            raise ValidationError("Passwords don't match!")
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="You can change password using <a href=\"../password/\">this form</a>"
    )

    class Meta:
        model = User
        fields = ('email', 'phone', 'password', 'is_active', 'is_admin')


# User login and registration
class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email address'})
    )
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Your password'}
    ))
