from django.shortcuts import render,redirect
from core.forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group

# Create your views here.

def base(request):
    return render(request,'core/base.html')

def login(request):
    return render(request,'core/login.html')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            group_id = form.cleaned_data['groups'].id  
            group = Group.objects.get(pk=group_id) 
            user.save()  
            user.groups.add(group)  
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})
