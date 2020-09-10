from django.urls import path
from RecuirtmentSystem import views

urlpatterns = [
    path('', views.root),
    path('home/', views.home, name="home"),
    path('company/',views.company,name="company")
]