from django import forms
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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
    
class UserUpdateForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
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

    def save(self, commit=True):

        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user


    def clean_email(self):
        
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    forms.ValidationError('This e-mail already exists.')
            )
        
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except forms.ValidationError as errors:
                self.add_error(
                    'password1',
                    forms.ValidationError(errors)
                )
        
        return password1
    
    def clean(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    forms.ValidationError('Passwords must be the same')
                )

        return super().clean()