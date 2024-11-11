from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us', views.about, name="about"),
    path('contact-us', views.contact, name="contact"),
    path('tours', views.tours, name="tours"),
    path('visas', views.visas, name="visas"),
    path('visa/<slug>', views.visa_detail, name="visa-detail"),
    path('flight-booking', views.flight_booking, name="flight-booking"),
    path('tour-booking/<slug>', views.tour_booking, name="tour-booking"),
    path('visa-booking/<slug>', views.visa_booking, name="visa-booking"),
    path('tour/<slug>', views.tour_detail, name="tour-detail"),
    path('search', views.search, name="search"),
    path('courses', views.courses, name="courses"),
    path('course/<slug>', views.course_booking, name="course-booking"),
    path('verify-payment/<str:ref>/', views.verify_payment, name='verify_payment'),
    path('filter-tours/', views.price_slider, name='price-slider'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)