from django import forms
from .models import YTVideo

class YTVideoForm(forms.ModelForm):
    class Meta:
        model = YTVideo
        fields = ('title', 'url')

    def clean(self):
        # do form checking here
        super().clean()
