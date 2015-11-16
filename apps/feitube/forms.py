from django import forms

class VideoForm(forms.Form):
    title = forms.CharField(max_length=255)
    tags = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1024)
    file = forms.FileField()