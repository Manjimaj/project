from django import forms
from app1.models import Data

class Dataform(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"
