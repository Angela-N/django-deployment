from django import forms
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User


# base form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileInfoForm(forms.ModelForm):
    # portfolio = forms.URLField(required=False)
    # picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfileInfo
        # exclude = ('user',)
        fields = ['portfolio', 'picture']
