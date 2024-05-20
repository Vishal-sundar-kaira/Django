from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', views.signup, name='signup'),  # Render signup.html
    path('login/', views.login_view, name='login'),  # Render login.html
    path('logout/', views.logout_view, name='logout'),  # Render logout.html
    path('dashboard/', views.dashboard, name='dashboard_data'),
     path('dashboard_data/', views.dashboard_data, name='dashboard_data'),
    path('chart-data/', views.chart_data, name='chart_data'),
    path('api/signup/', views.SignUpView.as_view(), name='api_signup'),  # API endpoint for signup
    path('add_income/', views.IncomeSourceCreateView.as_view(), name='add_income'),
    path('add_expense_category/', views.ExpenseCategoryCreateView.as_view(), name='add_expense_category'),
    path('transactions/', views.TransactionListView.as_view(), name='transaction_list'),
    path('transaction/add/', views.TransactionCreateView.as_view(), name='transaction_add'),
    path('transaction/<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='transaction_edit'),
    path('transaction/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', views.LoginView.as_view(), name='api_login'),
    path('api/logout/', views.LogoutView.as_view(), name='api_logout'),
]
