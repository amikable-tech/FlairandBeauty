from django.shortcuts import render
from .forms import BookingForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, "website/home.html")

def jobs(request):
    return render(request, "website/jobs.html")

def team(request):
    return render(request, "website/jobs.html")


def booking(request):	
	submitted = False
	if request.method == "POST":
		booking_form = BookingForm(request.POST)
		if booking_form.is_valid():
			booking_form.save()
			return HttpResponseRedirect('booking_success')
	else:
		booking_form = BookingForm()
		if 'submitted' in request.GET:
			submitted = True
	return render (request, 'website/booking.html', { 'booking_form': booking_form, 'submitted': submitted }) 
