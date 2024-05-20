from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import IncomeSourceSerializer, ExpenseCategorySerializer, TransactionSerializer,UserSerializer
from .models import IncomeSource, ExpenseCategory, Transaction
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def dashboard_data(request):
    print("here came")
    user =User
    total_income = IncomeSource.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = ExpenseCategory.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
    savings = total_income - total_expenses

    return Response({
        'total_income': total_income,
        'total_expenses': total_expenses,
        'savings': savings
    })

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def chart_data(request):
    user = request.user
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)

    daily_income = IncomeSource.objects.filter(user=user, date=today).aggregate(total=Sum('amount'))['total'] or 0
    weekly_income = IncomeSource.objects.filter(user=user, date__gte=start_of_week).aggregate(total=Sum('amount'))['total'] or 0
    monthly_income = IncomeSource.objects.filter(user=user, date__gte=start_of_month).aggregate(total=Sum('amount'))['total'] or 0

    daily_expenses = ExpenseCategory.objects.filter(user=user, date=today).aggregate(total=Sum('amount'))['total'] or 0
    weekly_expenses = ExpenseCategory.objects.filter(user=user, date__gte=start_of_week).aggregate(total=Sum('amount'))['total'] or 0
    monthly_expenses = ExpenseCategory.objects.filter(user=user, date__gte=start_of_month).aggregate(total=Sum('amount'))['total'] or 0

    data = {
        "daily_income": daily_income,
        "weekly_income": weekly_income,
        "monthly_income": monthly_income,
        "daily_expenses": daily_expenses,
        "weekly_expenses": weekly_expenses,
        "monthly_expenses": monthly_expenses,
    }

    return Response(data)
def signup(request):
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    return render(request, 'logout.html')

class SignUpView(APIView):
    print("in views")
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Login successful"}, status=200)
        else:
            return Response({"detail": "Invalid credentials"}, status=400)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"detail": "Logout successful"}, status=200)

class IncomeSourceCreateView(generics.CreateAPIView):
    serializer_class = IncomeSourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseCategoryCreateView(generics.CreateAPIView):
    serializer_class = ExpenseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionUpdateView(generics.UpdateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionDeleteView(generics.DestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
