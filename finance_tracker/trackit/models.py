from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class IncomeSource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.amount}"

class ExpenseCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.amount}"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.category} - {self.amount}"

# Signals to create Transaction from Income and Expense

@receiver(post_save, sender=IncomeSource)
def create_transaction_from_income(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            user=instance.user,
            category='Income',
            amount=instance.amount,
            description=instance.description,
            date=instance.date
        )

@receiver(post_save, sender=ExpenseCategory)
def create_transaction_from_expense(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            user=instance.user,
            category='Expense',
            amount=instance.amount,
            description=instance.description,
            date=instance.date
        )
