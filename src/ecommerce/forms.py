from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter your name"
                   }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control",
                   "id": "full_email",
                   "placeholder": "Enter your email"
                   }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control",
                   "placeholder": "Enter your content"
                   }
        )
    )

    def clean_email(self):
        email = self.cleaned_data["email"]

        if "gmail" not in email:
            raise forms.ValidationError("Email has to contain gmail")

        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]

        if len(username) < 4:
            raise forms.ValidationError("Not a valid username")
        return username


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)

        if qs.exists():
            raise forms.ValidationError('Username already exist')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)

        if qs.exists():
            raise forms.ValidationError('Email already exists')

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Password must match!")

        return data
