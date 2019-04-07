from django.forms import ModelForm
from .models import WICS

class WICSForm(ModelForm):
    class Meta:
        model = WICS
        fields = '__all__'
