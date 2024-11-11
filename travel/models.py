from django.db import models
from django_resized import ResizedImageField
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from .paystack  import  Paystack
import secrets

# Create your models here.

class Tour(models.Model):
    slug = models.SlugField(max_length=150, blank=True, null=True)
    name = models.CharField( max_length=150)
    location = models.CharField( max_length=50)
    group = models.IntegerField()
    days = models.IntegerField()
    nights = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField(help_text="in %", blank=True, null=True)
    overview = models.TextField()
    date_depart = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_return = models.DateTimeField(auto_now=False, auto_now_add=False)
    tour_highlight_1 = models.CharField( max_length=200)
    tour_highlight_2 = models.CharField( max_length=200)
    tour_highlight_3 = models.CharField( max_length=200)
    tour_highlight_4 = models.CharField( max_length=200)
    tour_highlight_5 = models.CharField( max_length=200)
    tour_highlight_6 = models.CharField( max_length=200)
    image_1 = ResizedImageField(size=[600, 500], quality=100, crop=['middle', 'center'], upload_to='tours')    
    image_2 = ResizedImageField(size=[600, 500], quality=100, crop=['middle', 'center'], upload_to='tours', blank=True, null=True)    
    image_3 = ResizedImageField(size=[600, 500], quality=100, crop=['middle', 'center'], upload_to='tours', blank=True, null=True)    
    image_4 = ResizedImageField(size=[600, 500], quality=100, crop=['middle', 'center'], upload_to='tours', blank=True, null=True)    
    image_5 = ResizedImageField(size=[600, 500], quality=100, crop=['middle', 'center'], upload_to='tours', blank=True, null=True)    
    image_6 = ResizedImageField(size=[600, 500], quality=100, crop=['middle', 'center'], upload_to='tours', blank=True, null=True)    
    inclusion_1 = models.CharField(max_length=100)
    inclusion_2 = models.CharField(max_length=100)
    inclusion_3 = models.CharField(max_length=100)
    inclusion_4 = models.CharField(max_length=100)
    inclusion_5 = models.CharField(max_length=100)
    inclusion_6 = models.CharField(max_length=100)
    exclusion_1 = models.CharField(max_length=100, blank=True, null=True)
    exclusion_2 = models.CharField(max_length=100, blank=True, null=True)
    exclusion_3 = models.CharField(max_length=100, blank=True, null=True)
    exclusion_4 = models.CharField(max_length=100, blank=True, null=True)
    exclusion_5 = models.CharField(max_length=100, blank=True, null=True)
    exclusion_6 = models.CharField(max_length=100, blank=True, null=True)
    



    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
    
    def discounted_price(self):
        # Ensure self.discount is not None, set it to 0 if it is
        discount = self.discount if self.discount is not None else 0
        return self.price - ((discount / 100) * self.price)


class Itinerary(models.Model):
    slug = models.SlugField(max_length=150, blank=True, null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    day = models.IntegerField()
    description = models.TextField()
    location = models.CharField( max_length=50)
    image_1 = ResizedImageField(size=[400, 300], quality=100, crop=['middle', 'center'], upload_to='itineraries', blank=True, null=True)    
    image_2 = ResizedImageField(size=[400, 300], quality=100, crop=['middle', 'center'], upload_to='itineraries', blank=True, null=True)    
    image_3 = ResizedImageField(size=[400, 300], quality=100, crop=['middle', 'center'], upload_to='itineraries', blank=True, null=True)    
    image_4 = ResizedImageField(size=[400, 300], quality=100, crop=['middle', 'center'], upload_to='itineraries', blank=True, null=True)    
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Itineraries'

class Tour_Hotel(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    amenity_1 = models.CharField(max_length=100, blank=True, null=True)
    amenity_2 = models.CharField(max_length=100, blank=True, null=True)
    amenity_3 = models.CharField(max_length=100, blank=True, null=True)
    amenity_4 = models.CharField(max_length=100, blank=True, null=True)
    amenity_5 = models.CharField(max_length=100, blank=True, null=True)
    amenity_6 = models.CharField(max_length=100, blank=True, null=True)
    image = ResizedImageField(size=[400, 300], quality=100, crop=['middle', 'center'], upload_to='tour_hotel', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tour Hotels'

class Course(models.Model):
    slug = models.SlugField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150)
    duration = models.IntegerField()
    price = models.IntegerField()
    detail_1 = models.CharField(max_length=150)
    detail_2 = models.CharField(max_length=150)
    detail_3 = models.CharField(max_length=150)
    detail_4 = models.CharField(max_length=150)
    detail_5 = models.CharField(max_length=150, blank=True, null=True)
    detail_6 = models.CharField(max_length=150, blank=True, null=True)
    detail_7 = models.CharField(max_length=150, blank=True, null=True)
    detail_8 = models.CharField(max_length=150, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class Course_Booking(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()

    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

class Payments(models.Model):
    course = models.ForeignKey("Course", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=70)    
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f"Payment: ₦{self.amount} | by {self.name} {self.email}"

    def amount_value(self):
        return int(self.amount) * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payments.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Payments'

class Flight(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    from_location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)

class Visa(models.Model):
    slug = models.SlugField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class Tour_Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()

class Visa_Booking(models.Model):
    visa = models.ForeignKey(Visa, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()