# from typing import Any
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django import forms

#customizing the django 'UserCreationForm' to our needs
class CustomUserCreationForm(UserCreationForm):
    # username = forms.CharField(max_length=20, required=False)
    # email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields =['username','email','password1','password2']
        labels ={
            'username':'User Name',
            'email':'E-mail',
            'password1':'Password',
            'password2':'Confirm Password',
        }

    def __init__(self, *args,**kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)  
        self.fields['username'].widget.attrs.update({'class':'u_name','autocomplete':"off",'placeholder':'Enter username..'})
        self.fields['email'].widget.attrs.update({'class':'u_email'})
        self.fields['password1'].widget.attrs.update({'class':'u_pass'})
        self.fields['password2'].widget.attrs.update({'class':'u_pass'})