from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
service_options = [
    ('', 'Select'),
    ('Hair_cuts', 'Hair cuts and styling'),
    ('Glossing', 'Glossing'),
    ('Hair_dye', 'Hair coloration and dyeing')

] 

class appointment(models.Model):
    first_name = models.CharField('First Name', max_length=100, blank=False)
    last_name = models.CharField('Last Name', max_length=100, blank=False)
    email = models.EmailField(max_length=225, blank=False)
    phone_number = PhoneNumberField(blank=False)
    date_time = models.DateTimeField(blank=False)
    services = models.CharField(max_length= 50, choices=service_options, default='')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.date_time} - {self.services}'
    

class Weblink(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return f'{self.title}, {self.url}'