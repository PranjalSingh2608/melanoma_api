from django import forms
from .models import ImageClassify

class ImageForm(forms.ModelForm):
    class Meta:
        model=ImageClassify
        fields='__all__'