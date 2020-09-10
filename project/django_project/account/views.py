from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Employeeinfo, Companyinfo, User
import requests


# Create your views here.
def register(request) :
    if request.method == 'POST' :
        username = request.POST[ 'Username' ]
        password = request.POST[ 'Password' ]
        confirm = request.POST[ 'Confirm' ]
        gender = request.POST[ 'Gender' ]
        email = request.POST[ 'Email' ]
        address = request.POST[ 'Address' ]
        phone = request.POST[ 'Phone' ]

        response = requests.get(
            'https://jsonplaceholder.typicode.com/todos/1')
        # f'https://app.verify-email.org/api/v1/UBTW2fIw7W2yR5ICPldZGuah72wKN8gTsAB7aho06HoiKw9ySC/verify/{email}')
        data = response.json();
        if (data[ 'id' ] == 1) :  # status=1
            if password == confirm:
                try:
                    user = User.objects.get(username = username)
                    return render(request, 'account/register.html', {'error' : "username already registered!!"})
                except User.DoesNotExist:
                    user = User(username = username, password = password, is_employee = True)
                    user.save()
                    employee = Employeeinfo.objects.create(user = user, Gender = gender, Email = email,
                                                           Address = address, Phone = phone)
                    employee.save()
                    auth.login(request, user)
                    return redirect('home')

            else:
                return render(request, 'account/register.html', {'error' : 'Error password didn\'t match!!!'})

        else :
            return render(request, 'account/register.html', {'error' :'Invalid Email id'})
    else :
        return render(request, 'account/register.html')


def login(request) :
    if request.method == 'POST' :
        try :
            user = User.objects.get(username = request.POST[ "username" ], password = request.POST[ "password" ],
                                    is_employee = True)
            auth.login(request, user)
            return redirect('home')

        except User.DoesNotExist :
            return render(request, 'account/login.html', {'error' :"Username or password didn't match!!!"})

    else :
        return render(request, 'account/login.html')


def registerCompany(request):
    if request.method == 'POST':
        cname = request.POST['Cname']
        password = request.POST['Password']
        confirm = request.POST[ 'Confirm' ]
        category = request.POST[ 'Category' ]
        email = request.POST[ 'Email' ]
        address = request.POST[ 'Address' ]
        phone = request.POST[ 'Phone' ]
        # api call
        response = requests.get(
            'https://jsonplaceholder.typicode.com/todos/1')
        # f'https://app.verify-email.org/api/v1/UBTW2fIw7W2yR5ICPldZGuah72wKN8gTsAB7aho06HoiKw9ySC/verify/{email}')
        data = response.json();
        if (data[ 'id' ] == 1) :  # status=1
            if password == confirm :
                try :
                    user = User.objects.get(username = cname)
                    return render(request, 'account/register.html', {'error' :"company name already registered!!"})
                except User.DoesNotExist:

                    user = User(username = cname, password = password, is_company = True)
                    user.save()
                    company = Companyinfo.objects.create(user = user, Category = category, Email = email,
                                                         Address = address,
                                                         Phone = phone)
                    company.save()
                    auth.login(request, user)
                    return redirect('company')

            else :
                return render(request, 'account/register.html', {'error' :'Error password didn\'t match!!!'})

        else :
            return render(request, 'account/register.html', {'error' :'Invalid Email id'})
    else :
        return render(request, 'account/register.html')


def loginCompany(request) :
    if request.method == 'POST' :
        try:
            user = User.objects.get(username = request.POST[ "cname" ], password = request.POST[ "password" ],
                                    is_company = True)
            auth.login(request, user)
            return redirect('company')

        except User.DoesNotExist:
            return render(request, 'account/login.html', {'error' : "Company Name or password didn't match!!!"})

    else :
        return render(request, 'account/login.html')


def logout(request) :
    auth.logout(request)
    return redirect('login')
