from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .models import UserType,UserTypeRole,InvestorDocumentManager

def render_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    if user.usertype.user_type.role=='INVESTOR':
                        return HttpResponseRedirect('/investor/investor_details/')
                    elif user.usertype.user_type.role=='DEPOSITORY':
                        return HttpResponseRedirect('/depository/depository_dashboard/')
                    elif user.usertype.user_type.role=='ADMIN':
                        return HttpResponseRedirect('/forms9_admin/admin_dashboard/')
        else:
            form = LoginForm()
        return render(request,'partials/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/')

from django.contrib.auth.forms import UserCreationForm

def render_register(request):
    if request.method=='POST':
        response_data ={}
        try:
            if not User.objects.filter(username=request.POST.get('email')).exists():
               
                username = request.POST.get('username')
                password = request.POST.get('password')
                last_name = request.POST.get('last_name','')
                first_name = request.POST.get('first_name','')

                user = User.objects.create(username= username,password=make_password(password),first_name=first_name,last_name=last_name,)
                try:
                    user_type, created = UserType.objects.update_or_create(
                    user=user,
                    defaults={
                        'user_type':UserTypeRole.objects.get(role='INVESTOR'),
                    })
                    if user is not None:
                        login(request,user)
                        if user.usertype.user_type.role=='INVESTOR':
                            return HttpResponseRedirect('/investor/investor_details/')
                        elif user.usertype.user_type.role=='DEPOSITORY':
                            return HttpResponseRedirect('/depository/depository_dashboard/')
                        elif user.usertype.user_type.role=='ADMIN':
                            return HttpResponseRedirect('/forms9_admin/admin_dashboard/')
                except Exception as e:
                    print(e)
                response_data['message'] = 'Account Successfully created..'
                
            
            else:
                response_data['message'] = 'Email already exists'
            return redirect('login')
        except Exception as e:
                response_data['message'] = 'It Seems some error occured.'
    return render(request, 'partials/register.html')


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        if user.usertype.user_type.role=='INVESTOR':
            return HttpResponseRedirect('/investor/investor_dashboard/')
        elif user.usertype.user_type.role=='DEPOSITORY':
            return HttpResponseRedirect('/depository/depository_dashboard/')
        elif user.usertype.user_type.role=='ADMIN':
            return HttpResponseRedirect('/forms9_admin/admin_dashboard/')
    else:
        return render(request, 'partials/home.html')
    

