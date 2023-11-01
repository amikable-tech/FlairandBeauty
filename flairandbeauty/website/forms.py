from django import forms
from django.forms import ModelForm
from datetime import datetime,timedelta
from tempus_dominus.widgets import DateTimePicker
from .models import appointment


service_options = [
    ('', 'Select'),
    ('Hair_cuts', 'Hair cuts and styling'),
    ('Glossing', 'Glossing'),
    ('Hair_dye', 'Hair coloration and dyeing')

]

class BookingForm(ModelForm):
    class Meta:
        model = appointment
        fields = '__all__'
        widgets = {
            'date_time': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                    'minDa  te': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
                    'maxDate': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'),
                    'disabledTimeIntervals': [
                        [datetime(1900, 1, 1, 12, 0).strftime('%H:%M'), datetime(1900, 1, 1, 13, 30).strftime('%H:%M')],
                    ],
                    'daysOfWeekDisabled': [0, 6],  
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            )
        }

