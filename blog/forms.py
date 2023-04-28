from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    text = forms.CharField(widget=forms.Textarea(attrs={'label': 'Text'}))