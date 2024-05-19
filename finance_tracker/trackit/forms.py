
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import IncomeSource, ExpenseCategory, Transaction

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class IncomeSourceForm(forms.ModelForm):
    class Meta:
        model = IncomeSource
        fields = ['name', 'amount', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['name', 'amount', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'date', 'description']
