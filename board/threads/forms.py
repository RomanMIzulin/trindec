from django import forms

class text_of_post(forms.Form):
    text = forms.CharField(label = 'Ur text', max_length = 2048)
