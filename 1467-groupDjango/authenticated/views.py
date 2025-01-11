from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             messages.success(request, "Xush kelibsiz")
#             return redirect("manu")
#
#         else:
#             messages.success(request, "Parol yoki Username xato kiritdingiz")
#             return redirect("login")
#     return render(request, 'auth/login.html')
#
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Xush kelibsiz")
            return redirect("manu")
        else:
            messages.error(request, "Parol yoki Username xato kiritdingiz")
            return redirect("login")

    return render(request, 'auth/login.html')


def register_view(request):
    return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Siz saytdan chiqib ketdingiz!!!")
    return redirect('login')


def profile_view(request):
    return render(request, 'auth/profile.html')
