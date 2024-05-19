from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),  # Auth URLs
    path('signup/', views.signup, name='signup'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense_category/', views.add_expense_category, name='add_expense_category'),
    # path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('transactions/', views.TransactionListView.as_view(), name='transaction_list'),
    path('transaction/add/', views.TransactionCreateView.as_view(), name='transaction_add'),
    path('transaction/<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='transaction_edit'),
    path('transaction/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),
]
