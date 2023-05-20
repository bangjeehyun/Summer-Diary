from django.shortcuts import render

def base(request): #메인페이지
    return render(request, 'Posts/base.html')

def mypage(request): #마이페이지
    return render(request, 'Posts/mypage.html')

def writing(request): #게시물 작성
    return render(request, 'Posts/writing.html')
