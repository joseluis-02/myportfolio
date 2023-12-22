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
        fields=('__all__')