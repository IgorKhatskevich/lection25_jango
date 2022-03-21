from django import forms


class BookForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)
    pages_number = forms.IntegerField(label="Pages number")
    description = forms.CharField(label="Description", widget=forms.Textarea)


class ReviewForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class EditBookDescriptionForm(forms.Form):
    description = forms.CharField(label="Description", widget=forms.Textarea)