from django.contrib import admin
from .models import IncomeSource, ExpenseCategory, Transaction

admin.site.register(IncomeSource)
admin.site.register(ExpenseCategory)
admin.site.register(Transaction)