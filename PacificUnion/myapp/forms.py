from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    firstname = forms.CharField(max_length=10, required=True)
    lastname = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(max_length=30, required=True)
    phonenumber = forms.CharField(max_length=10, required=True)
    GENDER_CHOICES = (
        ('Gender', 'Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    STATUS = (
        ('Status', 'Status'),
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Retired', 'Retired'),
        ('Disabled', 'Disabled'),
        )
    status = forms.ChoiceField(choices=STATUS)
    ACCOUNT_TYPE_CHOICES = (
        ('Account Type', 'Account Type'),
        ('Online Account', 'Online Account'),
        ('Savings Account', 'Saving Account'),
        ('Fixed Account', 'Fixed Account'),
        ('Shared Account', 'Shared Account'),
        )
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES)
    CURRENCY_CHOICES = (
    ('USD', 'United States Dollar'),
    ('EUR', 'Euro'),
    ('JPY', 'Japanese Yen'),
    ('GBP', 'British Pound'),
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('CHF', 'Swiss Franc'),
    ('CNY', 'Chinese Yuan'),
    ('SEK', 'Swedish Krona'),
    ('NZD', 'New Zealand Dollar'),
    # Add more currencies as needed
     )
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)



class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'firstname', 'lastname', 'status', 'currency', 'gender', 'account_type', 'phonenumber']

