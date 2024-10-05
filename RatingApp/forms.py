from django import forms
from .models import SecondYear,ThirdYear,User

class SecondYearForm(forms.ModelForm):
    class Meta:
      model = SecondYear
      exclude = ['user','id']

class ThirdYearForm(forms.ModelForm):
    class Meta:
      model = ThirdYear
      exclude = ['user','id']


class UserNameForm(forms.ModelForm):
   class Meta:
      model = User
      fields = '__all__'
      widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form_name',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form_email',
                'placeholder': 'Enter your email',
            }),
        }
