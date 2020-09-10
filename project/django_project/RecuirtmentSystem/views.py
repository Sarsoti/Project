from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.decorators import company_required

# Create your views here.
def root(request):
    return redirect('home')

def home(request):
    return render(request,'RecuirtmentSystem/home.html')

@login_required(login_url="/account/logincompany/")
@company_required
def company(request):
    return render(request,'RecuirtmentSystem/company.html')