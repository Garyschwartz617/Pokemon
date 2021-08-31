from .models import Response
from django import forms


class CreateResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('card_buyer','amount')
