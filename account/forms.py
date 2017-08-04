from django import forms

class LoginForm(forms.Form):
    """Definicja formularza logowania.
    Wymienia pola, które formularz będzie prezentował."""
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)