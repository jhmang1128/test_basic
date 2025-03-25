from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .forms import UserChangeForm_custom, UserCreationForm_custom


# def deco_print(func):
#     def return_func():
#         print("\n")
#         func()
#         print("\n")
#     return return_func


####################################################################################################################
#### user log in & out
####################################################################################################################

#### log-in
@require_http_methods(["GET", "POST"])
def login(request): 
    if request.method == "POST": # 로그인 실행
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
        
    else: # 로그인 창 진입
        form = AuthenticationForm()
        context = {"form" : form}
        return render(request, "user/login.html", context)


class Log_in_APIView(APIView):
    def post(self, request): # 로그인 실행
        # print("\n", request.data, "\n")
        # print("\n", request.POST, "\n")
        form = AuthenticationForm(data = request.data)
        if form.is_valid():
            auth_login(request, form.get_user())
            print_text = f"log-in {form.data["username"]}"
            
            return Response(print_text, status=200)
        else: return Response(form.errors, status=400)
            
        
        

#### log-out
@require_http_methods(["POST"])
@login_required
def logout(request): # 로그아웃 실행
    print(request)
    auth_logout(request)
    return redirect('index')


class Log_out_APIView(APIView):
    def post(self, request): # 로그아웃 실행
        auth_logout(request)
        print_text = "log out"
            
        return Response(print_text, status=200)


####################################################################################################################
#### user CRUD
####################################################################################################################

#### user - create
@require_http_methods(["GET", "POST"])
@csrf_exempt
def signup(request):
    if request.method == "POST": # user 회원 가입 실행
        form = UserCreationForm_custom(request.data)
        if form.is_valid():
            form.save()
            return redirect("index")
        
    else: # user 회원 가입 창 진입
        form = UserCreationForm_custom()
        context = {"form": form}
        return render(request, "user/signup.html", context)


class User_Create_APIView(APIView):
    def post(self, request): # user 회원 가입 실행
        form = UserCreationForm_custom(request.data)
        if form.is_valid():
            form.save()
            return Response(status=200)
        else: return Response(form.errors, status=400)



#### user - delete
@require_http_methods(["POST"])
@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('index')


class User_Delete_APIView(APIView):
    def post(self, request): # user 삭제 실행
        request.user.delete()
        auth_logout(request)
        return Response(status=200)


####################################################################################################################
#### profile CRUD
####################################################################################################################

#### profile
@require_http_methods(["GET", "POST"])
def profile(request): # 프로필 생성 실행
    if request.method == "POST":
        form = UserChangeForm_custom(request.data, instance=request.user) # 업데이트 폼 변경
        if form.is_valid():
            form.save()
            return redirect("index")
        
    else: # 프로필 창 접근
        form = UserChangeForm_custom(instance=request.user)
        context = {"form": form}
        return render(request, "user/profile.html", context)
    
    
class Profile_Create_APIView(APIView):
    def post(self, request): # 프로필 생성 실행
        form = UserChangeForm_custom(request.data, instance=request.user)
        if form.is_valid():
            form.save()
            return Response(status=200)
        else:
            return Response(form.error, status=400)