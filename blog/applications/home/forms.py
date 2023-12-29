#Django
from django import forms
#Models
from .models import Suscribers,Contact

#Forms
class SuscribersForm(forms.ModelForm):
    class Meta:
        model = Suscribers
        fields=(
            'email',
        )
        widgets = {
            'email':forms.EmailInput(
                attrs={
                    'placeholder': 'Tu correo electrónico',
                    'class':'miclase',
                }
            )
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=(
            'full_name',
            'email',
            'messagge',
        )
    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if not full_name:
            raise forms.ValidationError("Nombres no puede estar vacío")
        return full_name
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError("Email no puede estar vacío")
        return email
    def clean_messagge(self):
        messagge = self.cleaned_data['messagge']
        if not messagge:
            raise forms.ValidationError("Mensaje no puede estar vacío")
        return messagge