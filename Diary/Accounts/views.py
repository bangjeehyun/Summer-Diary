from django.shortcuts import render

def join(request): #회원가입
    return render(request, 'Accounts/join..html')

def login(request): #로그인
    return render(request, 'Accounts/login.html')
