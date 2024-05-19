from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import IncomeSource, ExpenseCategory, Transaction
from .forms import IncomeSourceForm, ExpenseCategoryForm, TransactionForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
@login_required
def home(request):
    return render(request, 'home.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    total_income = IncomeSource.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = ExpenseCategory.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
    savings = total_income - total_expenses
    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'savings': savings
    }
    return render(request, 'dashboard.html', context)

def add_income(request):
    if request.method == 'POST':
        form = IncomeSourceForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('home')
    else:
        form = IncomeSourceForm()
    return render(request, 'add_income.html', {'form': form})

def add_expense_category(request):
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('home')
    else:
        form = ExpenseCategoryForm()
    return render(request, 'add_expense_category.html', {'form': form})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'
    
    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)
        
        # Print the queryset for debugging
        print("User:", self.request.user, "- Queryset:", queryset)
        
        return queryset

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction_form.html'
    success_url = reverse_lazy('transaction_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction_form.html'
    success_url = reverse_lazy('transaction_list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)