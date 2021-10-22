from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import formdata
from customer.models import MyReview, ReviewData
from django.core.mail import send_mail
from websoftera.settings import EMAIL_HOST_USER


# import requests
# from urllib.parse import urlencode
# import googlemaps

# API_KEY = 'AIzaSyCebpGpghjM4sh_-VGEb02AJb-Q_law3NI'
# map_client = googlemaps.Client(API_KEY)

# data_type = "json"
# endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
# params = {"address": "Pune, Maharashtra, India", "key": API_KEY}
# url_params = urlencode(params)
# url = f"{endpoint}?{url_params}"
# print(url)
# sample = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyA8eaHt9Dh5H57Zh0xVTqxVdBFCvFMqFjQ"

# def extract_lat_lng(address_or_postalcode, data_type="json"):
#     endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
#     params = {"address": address_or_postalcode, "key": API_KEY}
#     url_params = urlencode(params)
#     url = f"{endpoint}?{url_params}"
#     r = requests.get(url)
#     if r.status_code in range(200,299):
#         return r.json()
#     return {}

# print(extract_lat_lng("Pune, Maharashtra, India"))



# Create your views here.
def index(request):
    reviews = MyReview.objects.all()
    data = {
        'reviews': reviews
    }
    return render(request, 'index2.html', data)

def send_mail_admin(message):
    admin_mail = "kunalumaji@gmail.com"
    try:
        send_mail("Request callback at better-clean", message,EMAIL_HOST_USER,[admin_mail], fail_silently=False)
    except Exception as e:
        print(e)

def request_form(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    message = request.POST.get('message')

    try:
        data = formdata.objects.create(name=name, email=email, phone=phone, message=message)
        data.save()
        admin_message = "Hey admin,\n\nYou have received callback request. Here are the details of the customer. \n\nCustomer name: %s \nCustomer phone: %s \nCustomer email: %s \nCustomer message: %s \n\nThank you"% (name,phone,email,message)
        send_mail_admin(admin_message)

        message = "Hey %s, \n\nWe have received your request. Our team will get in touch with you shortly.\n\nThank you\nTeam better-clean\n\n\nFor more details mail us at support@companymail.com"% (data.name)
        try:
            send_mail("Request at better-clean", message, EMAIL_HOST_USER,[data.email],fail_silently=False)
        except Exception as e:
            print(e)

        response = {'status': 1, 'message': "We will get in touch with you shortly", 'client': data.name}
        return JsonResponse(response)
    except:
        response = {'status': 0, 'message': "Please try after some time..."}
        return JsonResponse(response)