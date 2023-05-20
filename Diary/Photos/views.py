from django.shortcuts import render

def upload(request): #사진 업로드
    return render(request, "Photos/upload.html")

def frame(request): #사진 프레임 선택
    return render(request, 'Photos/frame.html')
