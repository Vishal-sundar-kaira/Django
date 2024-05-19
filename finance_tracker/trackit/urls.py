from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('accounts/', include('django.contrib.auth.urls')),  # Auth URLs
    path('signup/', views.signup, name='signup'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense_category/', views.add_expense_category, name='add_expense_category'),
    # path('add_transaction/', views.add_transaction, name='add_transaction'),
]
