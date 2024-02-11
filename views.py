from django.shortcuts import render,redirect,HttpResponseRedirect
from core.forms import CustomUserRegisterForm,CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import login,logout,authenticate
from core.models import JobHolderProfile,JobRecruiterProfile
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def base(request):
    return render(request,'core/base.html')

def register(request):
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            group_id = form.cleaned_data['groups'].id  
            group = Group.objects.get(pk=group_id) 
            user.save()  
            user.groups.add(group)  
            return redirect('/login/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = CustomAuthenticationForm(request=request, data=request.POST)

            if fm.is_valid():
                username = fm.cleaned_data['username']
                upassword = fm.cleaned_data['password']
                user = authenticate(username=username, password=upassword)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Welcome to Job Finder")
                    return HttpResponseRedirect('/')
                else:
                    print("user Not found")
        else:
            fm = CustomAuthenticationForm()
        return render(request, 'core/login.html', {"form": fm,"user":request.user})
    else:
        messages.error(request, "Please log out first to access this page")
        return HttpResponseRedirect('/profile/')
    
def user_logout(request):
    logout(request)
    messages.success(request,"user logout successfully")
    return HttpResponseRedirect('/login/')


def profile(request):
    if request.user.groups.filter(name="jobholder").exists():
        return render(request, 'core/jobholder_profile.html')
    else:
        return render(request, 'core/jobrecruiter_profile.html')
  
