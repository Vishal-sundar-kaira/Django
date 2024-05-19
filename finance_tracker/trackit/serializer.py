from rest_framework import serializers
from django.contrib.auth.models import User
from .models import IncomeSource, ExpenseCategory, Transaction
from django.contrib.auth.password_validation import validate_password

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user

class IncomeSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeSource
        fields = ['id', 'name', 'amount', 'description', 'date']

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name', 'amount', 'description', 'date']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'category', 'amount', 'description', 'date']
