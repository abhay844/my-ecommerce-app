from django import  forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
                widget=forms.TextInput(
                    attrs={"class":"form-control",
                           "placeholder":"Enter your name"
                           }
                   )
                )
    email = forms.EmailField(
                widget=forms.EmailInput(
                    attrs={"class":"form-control",
                           "id":"full_email",
                           "placeholder":"Enter your email"
                           }
                    )
                )
    content = forms.CharField(
                widget=forms.Textarea(
                    attrs={"class":"form-control",
                           "placeholder":"Enter your content"
                           }
                    )
                )

    def clean_email(self):
        email = self.cleaned_data["email"]

        if "gmail" not in email:
            raise forms.ValidationError("Email has to contain gmail")

        return email
