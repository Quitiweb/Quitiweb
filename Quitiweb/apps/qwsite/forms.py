from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'your@email.com'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'What do you want to say'}), required=True)
