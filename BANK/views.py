from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .decorators import ip_check
from .models import Account
from .serializers import AccountSerializer


class Helloview(APIView):

    def get(self,request, *args, **kwargs):
        request_ip = request.META['REMOTE_ADDR']
        return JsonResponse({'Message': 'You are ok'}, status=200)


class Accountlist(APIView):

    @method_decorator(ip_check)
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        account = Account.objects.create(
            account_number=request.data['account_number'],
            name=request.data['name'],
            phone_number=request.data['phone_number'],
            balance=request.data['balance'],
        )
        if account:
            return Response("Account Created Successfully", status=status.HTTP_201_CREATED)
        return Response("Failed", status=status.HTTP_400_BAD_REQUEST)