from django.contrib import admin
from . models import Tour, Itinerary, Tour_Hotel, Course, Course_Booking, Payments, Contact, Flight, Visa, Tour_Booking, Visa_Booking
# Register your models here.

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'group', 'days', 'nights', 'date_depart', 'date_return']
    list_filter = ['price', 'date_depart', 'date_return', 'days', 'nights']
    search_fields = ['name', 'price', 'group']

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ['title','day', 'description', 'location']

@admin.register(Tour_Hotel)
class Tour_HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name', 'location']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','price', 'duration', 'detail_1', 'detail_2', 'detail_3',  'detail_4']
    list_filter = ['price', 'duration']
    search_fields = ['name']

@admin.register(Course_Booking)
class Course_BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    search_fields = ['name', 'email']

@admin.register(Payments)
class  PaymentsAdmin(admin.ModelAdmin):
    list_display  = ["name", "email", "ref", 'amount', "verified", "date_created"]
    list_filter = ["date_created", "verified"]
    search_fields = ["name", "ref", "course__title" ]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'subject', 'message']
    search_fields = ['name',  'email']

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'from_location', 'destination', 'date']
    search_fields = ['name',  'email']

@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']

@admin.register(Tour_Booking)
class Tour_BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    search_fields = ['name', 'email', 'phone_number', 'tour__name']

@admin.register(Visa_Booking)
class Visa_BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    search_fields = ['name', 'email', 'phone_number', 'visa__name']
