from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import SpecialOffer, Room, Style, CoffeeBreak, Reservation
# Create your views here.

def index(request):
    return render(request,('index.html'))


def specialoffer(request):
    special_offers = SpecialOffer.objects.all()
    return render(request,('specialoffer.html'),{
        'special_offers': special_offers
    })

def room(request):
    rooms = Room.objects.all()
    return render(request,('room.html'),{
        'rooms': rooms
        })
    
def style(request):
    styles = Style.objects.all()
    return render(request,('style.html'),{
        'styles': styles
        })


def coffeebreak(request):
    coffeebreaks = CoffeeBreak.objects.all()
    return render(request,('coffeebreak.html'),{
        'coffeebreaks':coffeebreaks
    })
    


def reservation(request):
    rooms = Room.objects.all()
    styles = Style.objects.all()
    coffee_breaks = CoffeeBreak.objects.all()
    context = {
        'rooms': rooms,
        'styles': styles,
        'coffee_breaks': coffee_breaks,
    }
    if request.method == 'POST':
        event_space_1_id = request.POST['event_space_1']
        event_space_2_id = request.POST['event_space_2']
        coffee_break_id = request.POST['coffee_break']
        event_space_1 = request.POST.get('event_space_1')
        event_space_2 = request.POST.get('event_space_2')
        coffee_break = request.POST.get('coffee_break')
        date_and_time = request.POST.get('date_and_time')
        number_of_attendees = request.POST.get('number_of_attendees')
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        notes = request.POST.get('notes')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phone_number')
        event_space_1 = Room.objects.get(pk=event_space_1_id)
        event_space_2 = Style.objects.get(pk=event_space_2_id)
        coffee_break = CoffeeBreak.objects.get(pk=coffee_break_id)
        # Create a new reservation instance and save it
        reservation = Reservation(
            event_space_1=event_space_1,
            event_space_2=event_space_2,
            coffee_break=coffee_break,
            date_and_time=date_and_time,
            number_of_attendees=number_of_attendees,
            notes=notes,
            email=email,
            phone_number=phoneNumber,
            first_name=firstName,
            last_name=lastName,
        )
        reservation.save()
    return render(request, 'reservation.html',context)



def send_reservation_email(user_email, reservation_data):
    subject = 'Reservation Confirmation'
    message = f'Thank you for your reservation. Here are the details:\n\n{reservation_data}'
    from_email = 'settings.EMAIL_HOST_USER'  # Replace with your email
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
    
    return render('reservation.html')

# for the UserFavorite we shold do a urls so the user can go to it and view there favorite offer and have 
# a button so he can click it and see if it is still available or not 