from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import request
from myapp.models import Profile

# from myapp.models import Profile


class RegisterForm(forms.ModelForm):
    username=forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={'class':"form-control" })  )
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':"form-control" }))
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':"form-control" }))
    email=forms.EmailField(label="Email ID", required=True, widget=forms.TextInput(attrs={'class':"form-control" }))

    class Meta:
        model=User
        fields=('username', 'email')

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if email is None:
            raise forms.ValidationError("Email is required")
        return email


    def clean_password2(self):
        pass1= self.cleaned_data.get("password1")
        pass2= self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 != pass2 :
            raise forms.ValidationError("Password does not match")
        return pass2


    def save(self, commit=True):
        userobj= super(RegisterForm, self).save(commit=False)
        userobj.set_password(self.cleaned_data["password2"])
        if commit:
             userobj.save()
        return userobj

class LoginForm(forms.Form):
         username1=forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':"form-control" }))
         password1= forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':"form-control" }))

         def clean(self):
             uname=self.cleaned_data.get("username1")
             pass1=self.cleaned_data.get("password1")
             userobj= authenticate(request, username=uname, password=pass1)
             if userobj is None:
                 raise forms.ValidationError("Invalid username/ password")
             return super(LoginForm , self).clean()


class ProfileForm(forms.ModelForm):
      class Meta:
           model= Profile
           fields= ( "first_name","middle_name","last_name","birth_date",     "phone",  "address" )
           widgets={
                           "first_name": forms.TextInput(attrs={'class': "form-control"}),
                           "middle_name": forms.TextInput(attrs={'class': "form-control"}),
                           "last_name": forms.TextInput(attrs={'class': "form-control"}),
                           "birth_date": forms.TextInput(attrs={'class':"form-control" ,'placeholder':'yy/mm/dd'}),
                           "phone": forms.TextInput(attrs={'class': "form-control"}),
                           "address": forms.Textarea(attrs= {'class': "form-control", "rows":4 }),
                   }


