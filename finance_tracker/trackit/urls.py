from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('accounts/', include('django.contrib.auth.urls')),  # Auth URLs
    path('signup/', views.signup, name='signup'),
    # Add other URLs for your app here
]
