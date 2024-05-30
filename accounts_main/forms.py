from django import forms
from .models import User


class UserForm(forms.ModelForm):
   
    confirm_password = forms.CharField(widget= forms.PasswordInput())
    # confirm_password = forms.PasswordInput()
    
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone_number','email' ,'confirm_password', 'password',]
    
    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        
        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
        