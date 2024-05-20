from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  # Render signup.html
    path('login/', views.login_view, name='login'),  # Render login.html
    path('logout/', views.logout_view, name='logout'),  # Render logout.html
    path('dashboard/', views.dashboard, name='dashboard_data'),
    path('transactions/', views.transaction, name='transaction_list'),
     path('dashboard_data/', views.dashboard_data, name='dashboard_data'),
     path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('chart-data/', views.chart_data, name='chart_data'),
    path('api/signup/', views.SignUpView.as_view(), name='api_signup'),  # API endpoint for signup
    path('add_income/', views.add_income, name='add_income'),
    path('api/add_income/', views.IncomeSourceCreateView.as_view(), name='api_add_income'),
    path('add_expense_category/', views.ExpenseCategoryCreateView.as_view(), name='add_expense_category'),
    path('api/transactions/', views.TransactionListView.as_view(), name='transaction_lists'),
    
    path('transaction/add/', views.TransactionCreateView.as_view(), name='transaction_add'),
    path('transaction/<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='transaction_edit'),
    path('transaction/<int:pk>/ed/', views.editit, name='transaction_edit_it'),
    path('transaction_confirm',views.deleteit,name='transaction_confirm_delete'),

    path('transactions/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', views.LoginView.as_view(), name='api_login'),
    path('api/logout/', views.LogoutView.as_view(), name='api_logout'),
]
