from django import forms
class RegForm(forms.Form):
     username=forms.CharField(required=True,)
     email=forms.EmailField(required=True,)
     password=forms.CharField(required=True,)
     confirm_Password=forms.CharField(required=True,)