from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            "login_form": login_form
        }
        return render(request, "registration/login.html", context)
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "Siz muvaffaqiyatli hisobingizga kirdingiz 😎 !...")
            return redirect("home")
        context = {
            "login_form": login_form
        }
        messages.success(request, "Afsuski nimadur xato ketti 😔")
        return render(request, "registration/login.html", context)
    
class SignUpView(View):
    def get(self, request):
        signup_form = SignUpForm()
        context = {
            "signup_form": signup_form
        }
        return render(request, "registration/register.html", context)
    
    def post(self, request):
        signup_form = SignUpForm(data=request.POST, files=request.FILES)
        if signup_form.is_valid():
            user = signup_form.save(commit=True)
            login(request, user)
            messages.success(request, "Siz muvaffaqiyatli hisob yaratdingiz !...")
            return redirect("home")
        else:
            print("LOL !")
            context = {
            "signup_form": signup_form
            }
            messages.success(request, "Afsuski nimadur xato ketti 😔")
            return render(request, "registration/register.html", context)
    
class LogOutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Siz hisobingizdan chiqdingiz. Sizni yana kutib qolamiz 🙋‍♂️")
        return redirect("home")
    

class ProfilePageView(LoginRequiredMixin,View):
    def get(self, request):
        user = request.user
        context = {
            "user": user
        }
        return render(request, "users/profile.html", context)