from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import service_station, add_service, service_booking, CarService, CustomUser

# Create your views here.


@login_required
def addservicestation(request):
    user = request.user
    userid = user.id
    stnumber = range(1, 16)
    if request.method == 'POST':
        stname = request.POST.get('stname')
        ownername = request.POST.get('ownername')
        place = request.POST.get('loc')
        contact = request.POST.get('number')
        photo = request.FILES.get('photo')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        maxslot = request.POST.get('max_slot')
        available = maxslot
        date = datetime.now()
        description = request.POST.get('desc')
        price = request.POST.get('price')

        post = service_station(
            stname=stname,
            place=place,
            photo=photo,
            ownername=ownername,
            latitude=latitude,
            contact=contact,
            longitude=longitude,
            maxslot=maxslot,
            date=date,
            available=available,
            description=description,
            user_id=userid
        )
        post.save()

        return redirect('subscription')
    return render(request, "addservicestation.html", {'stnumber': stnumber})


def add_services(request, ser_id):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        photo = request.FILES.get('ser_img')
        ser_name = request.POST.get('ser_name')
        desc = request.POST.get('ser_desc')
        price = request.POST.get('ser_price')

        post = add_service(
            photo=photo,
            ser_name=ser_name,
            description=desc,
            price=price,
            service_id=ser_id,
        )
        post.save()

        return redirect('select_station')
    return render(request, "add_services.html",)


def service_home(request):
    return render(request, 'services_home.html')


def contact(request):
    return render(request, 'contact.html')


def select_station(request):
    stations = service_station.objects.all().order_by("-date")
    return render(request, "servicestation_list.html", {'data': stations})


def services(request, ser_id):
    ser_data = add_service.objects.filter(
        service_id=ser_id)  # Fix the model name
    return render(request, "bookservice.html", {'ser_data': ser_data, 'ser_id': ser_id})


def service_station_list(request):
    stations = service_station.objects.all().order_by("-date")
    return render(request, "servicestation_list.html", {'data': stations})

# def book(request):
#     stations = service_station.objects.all().order_by("-date")
#     return render(request,"bookservice.html",{'data': stations})


def myservice_station(request):
    user_id = request.user.id
    mystation = service_station.objects.filter(user_id=user_id, hidden=False)
    return render(request, "myservice_station.html", {'mystation': mystation})


# def bookservice(request):
#     user = request.user
#     userid = user.id
#     if request.method == 'POST':
#         ownername = request.POST.get('name')
#         phone = request.POST.get('phone')
#         company = request.POST.get('company')
#         model = request.POST.get('model')
#         km = request.POST.get('km')
#         date = request.POST.get('date')
#         type = request.POST.get('type')

#         # Get the selected checkboxes
#         car_services = request.POST.getlist('carServices')

#         post = service_booking(
#             ownername=ownername,
#             phone=phone,
#             company=company,
#             model=model,
#             date=date,
#             km_done=km,
#             type=type,
#             user_id_id=userid
#         )
#         post.save()

#         # Add related service instances for each selected checkbox
#         for service_name in car_services:
#             service_instance = CarService.objects.get_or_create(name=service_name)[
#                 0]
#             post.car_services.add(service_instance)

        


#         return redirect('service_home')
#     return render(request, "service_booking_form.html")


@login_required
def bookservice(request):
    if request.method == 'POST':
        # Extract data from the request.POST dictionary
        ownername = request.POST.get('name')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        model = request.POST.get('model')
        vehno = request.POST.get('vehno')
        km = request.POST.get('km')
        date = request.POST.get('date')
        type = request.POST.get('type')

        # Get the selected checkboxes
        car_services = request.POST.getlist('carServices')

        # Create a service booking instance
        booking = service_booking.objects.create(
            ownername=ownername,
            phone=phone,
            company=company,
            model=model,
            km_done=km,
            date=date,
            type=type,
            vehno=vehno,
            user_id=request.user
        )

        # Add related service instances for each selected checkbox
        for service_name in car_services:
            service_instance = CarService.objects.get_or_create(name=service_name)[0]
            booking.car_services.add(service_instance)

        # Save the service booking
        booking.save()

        # Send email to the user
        send_service_booking_email(request.user.email, booking)

        return redirect('service_home')

    return render(request, "service_booking_form.html")


from django.core.mail import EmailMessage
from django.conf import settings
def send_service_booking_email(user_email, booking):
    email_subject = 'Service Booking Confirmation'
    email_body = f'''
        Dear {booking.ownername},
        
        Your service booking has been confirmed successfully. Below are the details of your booking:
        
        Owner Name: {booking.ownername}
        Phone: {booking.phone}
        Company: {booking.company}
        Model: {booking.model}
        KM Done: {booking.km_done}
        Date: {booking.date}
        Type: {booking.type}
        
        Thank you for choosing our service!
    '''
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    email = EmailMessage(email_subject, email_body, from_email, recipient_list)
    email.send()


def worker_dash(request):
    user = request.user
    data = CustomUser.objects.filter(id=user.id)
    total_booking = service_booking.objects.filter(status=True).count()
    bookings = service_booking.objects.all()
    return render(request, "worker_dashboard.html", {'bookings': bookings, 'data': data, 'total_booking': total_booking})


def attend_service_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(service_booking, id=booking_id)
        booking.status = True
        booking.save()
        # Redirect to the worker dashboard or another page
        return redirect('worker_dash')
    return redirect('worker_dash')

def hide_ser_station(request,stid3):

    station_to_hide = service_station.objects.get(id=stid3)
    station_to_hide.hidden=True
    station_to_hide.save()
    return redirect('myservice_station')

def show_serstation(request, stid2):
    station_to_hide = get_object_or_404(service_station, id=stid2)
    station_to_hide.hidden = False
    station_to_hide.save()
    return redirect('myservice_station')

def closed_service_station(request):
    user_id = request.user.id
    mystation = service_station.objects.filter(user_id=user_id, hidden=True)
    return render(request, "service_shutdown.html", {'mystation': mystation})


def ser_update(request, stid2):
    myStation = service_station.objects.get(id=stid2)
    if request.method == 'POST':
        # Update the fields of the station object with the submitted data
        myStation.stname = request.POST.get('stname')
        myStation.ownername = request.POST.get('ownername')
        myStation.place = request.POST.get('place')
        myStation.latitude = request.POST.get('latitude')
        myStation.longitude = request.POST.get('longitude')
        myStation.maxslot = request.POST.get('maxslot')
        myStation.description = request.POST.get('description')
        myStation.contact = request.POST.get('contact')
        myStation.save()
        return redirect('myservice_station')
    else:
        return render(request, "ser_station_update.html", {'myStation': myStation})

def ser_delete(request, stid2):
    station_to_hide = get_object_or_404(service_station, id=stid2)
    station_to_hide.hidden = True
    station_to_hide.save()
    return redirect('myservice_station')

def delete_service(request, stid2):
    station_to_hide = get_object_or_404(add_service, id=stid2)
    station_to_hide.status = True
    station_to_hide.save()
    return redirect('myservice_station')

def mybooking(request):
    user_id = request.user.id
    booked_data =service_booking.objects.filter(user_id=user_id,deletee=False)
    return render(request,"service_booked.html",{'booked_data':booked_data})
    
def delete_my_ser_booked(request, stid2):
    station_to_hide = get_object_or_404(service_booking, id=stid2)
    station_to_hide.deletee = True
    station_to_hide.save()
    return redirect('http://127.0.0.1:8000/make_service/mybooking/')



def ser_station_booked(request):
    user = request.user
    data = CustomUser.objects.filter(id=user.id)
    total_booking = service_booking.objects.filter(status=True).count()
    bookings = service_booking.objects.all()
    return render(request, "station_own_dashboard.html", {'bookings': bookings, 'data': data, 'total_booking': total_booking})