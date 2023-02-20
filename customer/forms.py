from accounts.models import Account
from django.forms import ModelForm


class CustomerRegistrationForm(ModelForm):
    class Meta:
        model = Account