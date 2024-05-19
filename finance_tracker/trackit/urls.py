from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_data, name='dashboard_data'),
    path('chart-data/', views.chart_data, name='chart_data'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('add_income/', views.IncomeSourceCreateView.as_view(), name='add_income'),
    path('add_expense_category/', views.ExpenseCategoryCreateView.as_view(), name='add_expense_category'),
    path('transactions/', views.TransactionListView.as_view(), name='transaction_list'),
    path('transaction/add/', views.TransactionCreateView.as_view(), name='transaction_add'),
    path('transaction/<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='transaction_edit'),
    path('transaction/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),
    path('api-auth/', include('rest_framework.urls')),
]
