from django.urls import path
from core import views

urlpatterns = [
    path('test/',views.base),
    path('',views.login,name='login'),
    path('register',views.register,name='register'),
]
