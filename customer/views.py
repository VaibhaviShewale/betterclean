from django.contrib import auth
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def delete_review(request):
    if request.user.is_authenticated:
        delete = MyReview.objects.delete(user=request.user)
        delete.save()
        messages.success(request, "Review deleted successfully")
        return redirect("index")
    else:
        messages.warning(request, "Please login to continue")
        return redirect("login")

def update_review(request):
    if request.user.is_authenticated:
        pass
    else:
        messages.warning(request, "Please login to continue")
        return redirect("login")

    if request.method == "GET":
        obj = MyReview.objects.all(user=request.user)
        data = {
            'review':obj
        }
        return render(request, "review.html", data)
    else:
        return redirect("index")


def create_review(request):
    if request.user.is_authenticated:
        pass
    else:
        messages.warning(request, "Please login to continue")
        return redirect("login")

    if request.method == "GET":
        obj = MyReview.objects.filter(user=request.user)
        data = {
            'review': obj
        }
        return render(request, "review.html", data)
    else:
        review = request.POST.get("review")
        rating = request.POST.get("rating")

        try:
            create = MyReview.objects.create(user=request.user, rating=rating, review=review)
            create.save()
            messages.success(request, "Review created successfully")
            return redirect("index")
        except:
            messages.error(request, "Error while creating the request")
            return redirect("index")



class Review(View):
    def get(self, request):
        return render(request, "review.html")

    def post(self, request):
        cfname = request.POST.get("cfname")
        clname = request.POST.get("clname")
        ccity = request.POST.get("ccity")
        creview = request.POST.get("creview")
        # crating = request.POST.get("crating")
        crating = 4
        
        try:
            data = ReviewData.objects.create(cfname=cfname,clname=clname,ccity=ccity,creview=creview,crating=crating)
            data.save()
            return JsonResponse({'status': 1, 'message': "Your response has been recorded", 'cfname':data.cfname})
        except Exception as e:
            return JsonResponse({'status': 0, 'message': "", 'error': e})
     
def logout_user(request):
    logout(request)
    return redirect("index")

def register_user(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("index")
        else:
            return render(request, "register.html")
    
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')

        try:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
            user.save()
            login(request, user)
            return redirect("index")
        except:
            messages.error(request, "Something went wrong.")
            return redirect("register")

def login_user(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("index")
        else:
            return render(request, "login.html")
    
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid details")
            return redirect("login")