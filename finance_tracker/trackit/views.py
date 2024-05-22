from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import IncomeSourceSerializer, ExpenseCategorySerializer, TransactionSerializer,UserSerializer,GoalSerializer
from .models import IncomeSource, ExpenseCategory, Transaction, Goal
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
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from django.shortcuts import render, get_object_or_404
from .models import Transaction

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def dashboard_data(request):
    print("here came")
    user =request.user
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

@login_required
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    return render(request, 'login.html')

def add_income(request):
    return render(request, 'add_income.html')

def add_expense(request):
    return render(request, 'add_expense_category.html')

def transaction(request):
    return render(request, 'transaction_list.html')

def logout_view(request):
    auth_logout(request)
    return render(request, 'logout.html')

def add_transaction(request):
    return render(request, 'add_transaction.html')

def transaction_delete(request, pk):
    return render(request, 'transaction_confirm_delete.html', {'pk': pk})


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            logout(request)
            return Response({"detail": "Logout successful"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Token not found"}, status=status.HTTP_404_NOT_FOUND)

class IncomeSourceCreateView(generics.CreateAPIView):
    serializer_class = IncomeSourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoalListCreateView(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoalRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)


class ExpenseCategoryCreateView(generics.CreateAPIView):
    serializer_class = ExpenseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
def transaction_edit(request):
    return render(request, 'transaction_form.html')
class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionListView(generics.ListAPIView):
    print("here ok")
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionDeleteView(generics.DestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
