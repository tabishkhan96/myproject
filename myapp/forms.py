from django import forms
from .models import *

class myform(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = "__all__"