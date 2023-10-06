from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import SpecialOffer, Room, Style, CoffeeBreak, Reservation, ContactUs


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
        event_room_id = request.POST['event_room']
        event_style_id = request.POST['event_style']
        coffee_break_id = request.POST['coffee_break']
        event_room = request.POST.get('event_room')
        event_style = request.POST.get('event_style')
        coffee_break = request.POST.get('coffee_break')
        date_and_time = request.POST.get('date_and_time')
        number_of_attendees = request.POST.get('number_of_attendees')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        notes = request.POST.get('notes')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        event_room = Room.objects.get(pk=event_room_id)
        event_style = Style.objects.get(pk=event_style_id)
        coffee_break = CoffeeBreak.objects.get(pk=coffee_break_id)
        reservation = Reservation(
            event_room=event_room,
            event_style=event_style,
            coffee_break=coffee_break,
            date_and_time=date_and_time,
            number_of_attendees=number_of_attendees,
            notes=notes,
            email=email,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )
        reservation.save()
        send_mail('Reservation Confirmation',
                  render_to_string ('email.html', {'reservation': reservation}),
                  'eaxample@email.com',     #your email
            [request.POST.get('email')], fail_silently=False)
        #do not forget to put your email&app password in settings.py
    return render(request, 'reservation.html',context)


def contactUs(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactUs=ContactUs(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message,
            
        )
        contactUs.save()
        send_mail('Message Confirmation',
                  render_to_string ('contactMessage.html', {'contactUs': contactUs}),
                  'eaxample@email.com',     #your email
            [request.POST.get('email')], fail_silently=False)
        #do not forget to put your email&app password in settings.py
    return render(request, 'contactUs.html')
        
        