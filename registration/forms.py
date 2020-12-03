from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


from registration.utils import check_email


class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'invalid_email': _('Please enter a valid email')
    }

    class Meta:
        model = User
        fields = ('email',)
        field_classes = {'email': UsernameField}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not check_email(email):
            raise forms.ValidationError(
                self.error_messages['invalid_email']
            )
        return email
