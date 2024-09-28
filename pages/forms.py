from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':  "Name"}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'type': 'Email', 'placeholder': "Email"}))
    message = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'placeholder': "Message"}))