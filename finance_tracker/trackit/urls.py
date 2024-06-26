from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  # Render signup.html
    path('login/', views.login_view, name='login'),  # Render login.html
    path('logout/', views.logout_view, name='logout'),  # Render logout.html
    path('dashboard/', views.dashboard, name='dashboard_data'),
    path('transactions/', views.transaction, name='transaction_list'),
     path('dashboard_data/', views.dashboard_data, name='dashboard_data'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('chart-data/', views.chart_data, name='chart_data'),
    path('api/signup/', views.SignUpView.as_view(), name='api_signup'),  # API endpoint for signup
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    
     path('api/goals/', views.GoalListCreateView.as_view(), name='goal_list_create'),
    path('api/goals/<int:pk>/', views.GoalRetrieveUpdateView.as_view(), name='goal_detail_update'),
    path('api/add_income/', views.IncomeSourceCreateView.as_view(), name='api_add_income'),
    path('api/add_expense_category/', views.ExpenseCategoryCreateView.as_view(), name='add_expense_category'),
    path('api/transactions/', views.TransactionListView.as_view(), name='transaction_lists'),
    path('transaction/add/', views.TransactionCreateView.as_view(), name='transaction_add'),
    # path('transaction/<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='transaction_edit'),
     path('api/transactions/<int:pk>/', views.TransactionUpdateView.as_view(), name='transaction_detail'),
    path('api/transactions_add/', views.TransactionListCreateView.as_view(), name='transaction_list_create'),
    path('transaction_form/', views.transaction_edit, name='transaction_form'),
    # path('transaction/<int:pk>/ed/', views.editit, name='transaction_edit_it'),
     path('transaction_delete/<int:pk>/', views.transaction_delete, name='transaction_delete'),

    path('transactions/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', views.LoginView.as_view(), name='api_login'),
    path('api/logout/', views.LogoutView.as_view(), name='api_logout'),
]
