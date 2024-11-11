from django.shortcuts import render, redirect
from amadeus import Client, ResponseError, Location
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Tour, Itinerary, Tour_Hotel, Course, Course_Booking, Payments, Contact, Flight, Visa, Tour_Booking, Visa_Booking
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from mailjet_rest import Client
import os
import environ

env = environ.Env()
environ.Env.read_env()  # This will read variables from the .env file


SK = settings.SK
API_KEYY = settings.API_KEYY

def home(request):
    tours = Tour.objects.all().order_by('-id')[:6]
    tourss = Tour.objects.filter(discount__gt=0)
    courses = Course.objects.all().order_by('-id')[:3]
    visas = Visa.objects.all().order_by('-id')[:6]
    context = {'tours': tours, 'tourss': tourss, 'courses': courses, 'visas': visas}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about-us.html")

def tours(request):
    p = Paginator(Tour.objects.all().order_by('-id'), 5)
    page = request.GET.get('page')
    tours = p.get_page(page)
    context = {'tours': tours}
    return render(request, "tours.html", context)

def tour_detail(request, slug):
    tour = Tour.objects.get(slug=slug)
    tours = Tour.objects.all().order_by('-id')[:6]
    itineraries = Itinerary.objects.filter(tour=tour)
    try:
        tour_hotel = Tour_Hotel.objects.get(tour=tour)
    except Tour_Hotel.DoesNotExist:
        tour_hotel = None  # Handle the case where there are no matching results

    context = {'tour': tour, 'tours': tours, 'itineraries': itineraries, 'tour_hotel': tour_hotel}
    return render(request, "tour-detail.html", context)

from urllib.parse import urlencode

def search(request):
    # Get the search term from the POST request or query parameters
    searched = request.GET.get('q', request.POST.get('q', '')).strip()  # Use GET to persist the search query in pagination

    if searched:  # Ensure there's a valid search term
        tours = Tour.objects.filter(
            Q(location__icontains=searched) |
            Q(name__icontains=searched)
        ).order_by('id')  # Ensure results are ordered
    else:
        tours = Tour.objects.none()  # Return no results if no search term

    p = Paginator(tours, 3)  # Paginate with 1 tour per page
    page = request.GET.get('page', 1)  # Get the current page number, default to 1
    tours = p.get_page(page)

    # Create query parameters for pagination links
    query_params = urlencode({'q': searched}) if searched else ''

    return render(request, "search.html", {
        "searched": searched,
        "tours": tours,
        "query_params": query_params  # Pass query params to the template
    })



def price_slider(request):
    min_price = request.GET.get('min_price', 100000)  # Default value if not provided
    max_price = request.GET.get('max_price', 20000000)  # Default value if not provided
    
    tours = Tour.objects.filter(price__gte=min_price, price__lte=max_price)
    
    # Prepare data for JSON response
    data = {
        'tours': []
    }
    
    for tour in tours:
        data['tours'].append({
            'name': tour.name,
            'location': tour.location,
            'price': tour.price,
            'discount': tour.discount or 0,
            'slug': tour.slug,
            'url': reverse('tour-detail', args=[tour.slug])  # Generate URL for each tour
        })
    
    return JsonResponse(data)



def courses(request):
    courses = Course.objects.all().order_by('-id')
    context = {'courses': courses}
    return render(request,"course_pricing.html", context)

def course_booking(request, slug):
    course = Course.objects.get(slug=slug)
    if request.method == 'POST':
        course = Course.objects.get(slug=slug)
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        contact = Course_Booking(name=name, email=email, phone_number=phone_number, course=course)
        contact.save()
        pk = settings.PAYSTACK_PUBLIC_KEY
        payment = Payments.objects.create(amount=course.price, email=email, course=course, name=name)
        payment.save()
        
        context = {'course': course,
            'payment': payment,
            'field_values': request.POST,
            'paystack_pub_key': pk,
            'amount_value': payment.amount_value(),
            'course': course
            }
        return render(request, 'make_payment.html', context)
    return render(request, "course_pricing_form.html", {'course': course})


def verify_payment(request, ref):
    payment = Payments.objects.get(ref=ref)
    verified = payment.verify_payment()
    amount_paid = payment.course.price
    SK = settings.SK
    API_KEYY = settings.API_KEYY
    if verified:
        api_key = API_KEYY
        api_secret = SK
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
        'Messages': [
                        {
                                "From": {
                                        "Email": "bilahidcation@gmail.com",
                                        "Name": "Bilahid Cation"
                                },
                                "To": [
                                        {
                                                "Email": payment.email,
                                                "Name": payment.name
                                        }
                                ],
                                "Subject": "Course Booking",
                                "TextPart": f"Course: {payment.course.name}\nAvailability: {payment.course.duration}",
                                "HTMLPart": f"<h3>Dear {payment.name}, your booking for the course '{payment.course.name}' '₦{payment.course.price}' for {payment.course.duration} days,  has been received! Transaction number: {payment.ref}</h3><br />We will contact you shortly.<hr> Bilahid Cation"
                        }
                ]
        }
        result = mailjet.send.create(data=data)
        return render(request, "success.html")
    return render(request, "success.html", {"payment": payment})

def contact(request):
    SK = settings.SK
    API_KEYY = settings.API_KEYY
    if request.method == 'POST':
        api_key = API_KEYY
        api_secret = SK
        name = request.POST['name']
        phone_number = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, phone_number=phone_number, email=email, subject=subject, message=message)
        contact.save()
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
        'Messages': [
                        {
                                "From": {
                                        "Email": "bilahidcation@gmail.com",
                                        "Name": "Bilahid Cation"
                                },
                                "To": [
                                        {
                                                "Email": "bilahidcation@gmail.com",
                                                "Name": "Bilahid Cation"
                                        }
                                ],
                                "Subject": subject,
                                "TextPart": f"message: {message}",
                                "HTMLPart": f"<h3>Message '{message}' from '{name}', email address: {email} and phone number: {phone_number} "
                        }
                ]
        }
        result = mailjet.send.create(data=data)
        
        messages.success(request, 'Your message was received. We will get back to you shortly')
        return redirect("contact")
    return render(request, "contact.html")

def flight_booking(request):
    SK = settings.SK
    API_KEYY = settings.API_KEYY
    if request.method == 'POST':
        api_key = API_KEYY
        api_secret = SK
        name = request.POST['name']
        phone_number = request.POST['phone']
        email = request.POST['email']
        from_location = request.POST['from']
        destination = request.POST['destination']
        date = request.POST['date']
        flight = Flight(name=name, phone_number=phone_number, email=email, from_location=from_location, destination=destination, date=date)
        flight.save()
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
        'Messages': [
                        {
                                "From": {
                                        "Email": "bilahidcation@gmail.com",
                                        "Name": "Bilahid Cation"
                                },
                                "To": [
                                        {
                                                "Email": "bilahidcation@gmail.com",
                                                "Name": "Bilahid Cation"
                                        }
                                ],
                                "Subject": "Flight Booking",
                                "TextPart": f"message",
                                "HTMLPart": f"<h3>Flight booking from '{name}', email address: {email} and phone number: {phone_number}. From '{from_location}', to '{destination}' on '{date}' "
                        }
                ]
        }
        result = mailjet.send.create(data=data)
        
        messages.success(request, 'Your message was received. We will get back to you shortly')
        return redirect("home")
    return render(request, "flight_booking.html")

def visas(request):
    p = Paginator(Visa.objects.all().order_by('-id'), 6)
    page = request.GET.get('page')
    visas = p.get_page(page)
    context = {'visas': visas}
    return render(request, "visas.html", context)

def visa_detail(request, slug):
    visa = Visa.objects.get(slug=slug)
    context = {'visa': visa}
    return render(request, "visa-detail.html", context)

def tour_booking(request, slug):
    tour = Tour.objects.get(slug=slug)
    SK = settings.SK
    API_KEYY = settings.API_KEYY
    if request.method == 'POST':
        api_key = API_KEYY
        api_secret = SK
        tour = Tour.objects.get(slug=slug)
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        contact = Tour_Booking(name=name, email=email, phone_number=phone_number, tour=tour)
        contact.save()
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
        'Messages': [
                        {
                                "From": {
                                        "Email": "bilahidcation@gmail.com",
                                        "Name": "Bilahid Cation"
                                },
                                "To": [
                                        {
                                                "Email": "bilahidcation@gmail.com",
                                                "Name": "Bilahid Cation"
                                        }
                                ],
                                "Subject": "Flight Booking",
                                "TextPart": f"message",
                                "HTMLPart": f"<h3>Tour Booking from '{name}', email address: {email} and phone number: {phone_number}. for '{tour.name}' price '₦{tour.price}' "
                        }
                ]
        }
        result = mailjet.send.create(data=data)
        
        messages.success(request, 'Your message was received. We will get back to you shortly')
        
        context = {'tour': tour,
            }
        return render(request, 'tour_booking.html', context)
    return render(request, "tour_booking.html", {'tour': tour})

def visa_booking(request, slug):
    visa = Visa.objects.get(slug=slug)
    SK = settings.SK
    API_KEYY = settings.API_KEYY
    if request.method == 'POST':
        api_key = API_KEYY
        api_secret = SK
        visa = Visa.objects.get(slug=slug)
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        contact = Visa_Booking(name=name, email=email, phone_number=phone_number, visa=visa)
        contact.save()
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
        'Messages': [
                        {
                                "From": {
                                        "Email": "bilahidcation@gmail.com",
                                        "Name": "Bilahid Cation"
                                },
                                "To": [
                                        {
                                                "Email": "bilahidcation@gmail.com",
                                                "Name": "Bilahid Cation"
                                        }
                                ],
                                "Subject": "Visa Booking",
                                "TextPart": f"message",
                                "HTMLPart": f"<h3>Visa Booking from '{name}', email address: {email} and phone number: {phone_number}. for '{visa.name}' price '${visa.price}' "
                        }
                ]
        }
        result = mailjet.send.create(data=data)
        
        messages.success(request, 'Your message was received. We will get back to you shortly')
        
        context = {'visa': visa,
            }
        return render(request, 'visa_booking.html', context)
    return render(request, "visa_booking.html", {'visa': visa})