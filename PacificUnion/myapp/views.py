from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import *
from .models import *
from .decorators import *

@login_required(login_url='loginPage')
def home(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'balance':balance}
    return render(request, 'myapp/dashboard.html', context)

def analytics(request):
    return render(request, 'myapp/analytics.html')

def index(request):
    return render(request, 'myapp/index.html')

@login_required(login_url='loginPage')
def OTP(request):
    return render(request, 'myapp/dash.html')

@login_required(login_url='loginPage')
def profile(request):
    return render(request, 'myapp/profile.html')

@login_required(login_url='loginPage')
def deposit(request):
    return render(request, 'myapp/deposit.html')

@login_required(login_url='loginPage')
def pending(request):
    return render(request, 'myapp/pending.html')

@unauthenticated_user
def reg(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('firstname')
            messages.success(request, 'Your Account has been created successfully! '+ user)

            return redirect('login')

    context = {'form':form}
    return render(request, 'myapp/reg.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'myapp/loginPage.html', context)

@login_required(login_url='loginPage')
def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='loginPage')
def reports(request):
    return render(request, 'myapp/reports.html')

@login_required(login_url='loginPage')
def settings(request):
    return render(request, 'myapp/settings.html')

@login_required(login_url='loginPage')
def support_agent(request):
    return render(request, 'myapp/support_agent.html')

@login_required(login_url='loginPage')
def withdraw(request):
    return render(request, 'myapp/withdrawal.html')

@login_required(login_url='loginPage')
def Bank_transfer(request):
    return render(request, 'myapp/bnk.html')

@login_required(login_url='loginPage')
def trust_wise(request):
    return render(request, 'myapp/tw.html')

@login_required(login_url='loginPage')
def Google_pay(request):
    return render(request, 'myapp/gp.html')

@login_required(login_url='loginPage')
def skrill(request):
    return render(request, 'myapp/skrill.html')

@login_required(login_url='loginPage')
def Payoneer(request):
    return render(request, 'myapp/py.html')

@login_required(login_url='loginPage')
def PayPal(request):
    return render(request, 'myapp/PayPal.html')

@login_required(login_url='loginPage')
def Western_Union(request):
    return render(request, 'myapp/Western.html')

@login_required(login_url='loginPage')
def Crypto_page(request):
    return render(request, 'myapp/crypto_page.html')

@login_required(login_url='loginPage')
def index_page(request):
    return render(request, 'myapp/index_page.html')

@login_required(login_url='loginPage')
def details(request):
    form = Details.objects.all()
    object = get_object_or_404(Details)
    context = {'form':form, 'object':object}
    return render(request, 'myapp/details.html', context)