from django import forms
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
                    'placeholder': 'Enter the first name. (Required)'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the last name.'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the phone number. format: (**) *****-****. (Required)'
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

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        required=True
    )

    last_name = forms.CharField(
        required=True
    )

    email = forms.EmailField(
        required=True
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the first name.'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the last name.'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the email.'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the username.'
                }
            )
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                forms.ValidationError('This e-mail already exists.')
            )
        
        return email