from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import render,redirect
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate,login

from .serializers import TaskSerializer

from .models import login_data



def home(request):
    return render(request,'index.html')

@csrf_exempt
@api_view(['GET','POST'])
def login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if not username or not password:
                
                messages.success(request, 'Both Username and Password are required.')
                return redirect('/login')
            user_obj = login_data.objects.filter(username = username).first()
            if user_obj is None:
                print('hai')
                messages.success(request, 'User not found.')
                return redirect('/login')
        
            
            user = authenticate(username = username , password = password)
            
            if user is None:
                print('not found')
                messages.success(request, 'Wrong password.')
                return redirect('/login')
        
            login(request , user)
            
            #return redirect('/')
            return HttpResponse('sucessful')

                
            
            
    except Exception as e:
        print(e)
    return render(request , 'login.html')

    
@api_view(['GET','POST'])
def signup(request):
    try:
        if request.method == 'POST':
            
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

        try:
            
            if login_data.objects.filter(username = username).first():
                
                messages.success(request, 'Username is taken.')
                return redirect('/signup')
                #return HttpResponse('hai')

            if login_data.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/signup')
                #return HttpResponse('hai')
            
            #user_obj = login_data(username = username , email = email)
            
            #user_obj.set_password(password)
            #user_obj.save()
    
            profile_obj = login_data.objects.create(username = username , email = email,password=password)
            profile_obj.save()
            #return redirect('/login')
            return HttpResponse('hello')

        except Exception as e:
            print(e)

    except Exception as e:
            print(e)

   
    
    return render(request,'signup.html')



        
