from django import forms
from .models import ContactUs
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    name = forms.CharField(validators=[
        RegexValidator(r'[a-zA-Zа-яА-Я]+', 'Letters only!')
        ], widget=forms.TextInput(attrs={'placeholder' : "Ім'я", 'class': 'col-10'}))

    phone = forms.CharField(validators=[
        RegexValidator(r'[0-9]+', 'Numbers only!')
        ], widget=forms.TextInput(attrs={'placeholder' : "Номер телефону", 'class': 'col-10'}))
    
    category = forms.ChoiceField(choices=[('','Спосіб комунікації'), ('дзвінок','Дзвінок'),('viber', 'Viber'),('wats up', 'Wats up'),('telegram', 'Telegram'),], widget=forms.Select(attrs={'class': 'col-10'}))

class SnippetForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields = ('name', 'phone', 'communication_methods')