from django.urls import path
from account import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    #for company registration
    path('registercompany/',views.registerCompany,name="registercompany"),
    path('logincompany/',views.loginCompany,name="logincompany")

]