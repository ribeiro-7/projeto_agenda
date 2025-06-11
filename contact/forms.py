from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the first name. (Obrigatório)'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the last name.'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the phone number. format: (**) *****-****. (Obrigatório)'
                },
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the email.'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter the description.'
                }
            )
        }