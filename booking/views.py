from django.shortcuts import render, redirect
from .models import Service, Booking


def home(request):
    services = Service.objects.all()
    return render(request, "booking/home.html", {"services": services})


def book_service(request):

    if request.method == "POST":

        customer_name = request.POST["customer_name"]
        phone = request.POST["phone"]
        service_id = request.POST["service"]
        date = request.POST["date"]
        time_slot = request.POST["time_slot"]
        address = request.POST["address"]

        service = Service.objects.get(id=service_id)

        Booking.objects.create(
            customer_name=customer_name,
            phone=phone,
            service=service,
            date=date,
            time_slot=time_slot,
            address=address
        )

        return redirect("/")

    services = Service.objects.all()

    return render(
        request,
        "booking/booking.html",
        {"services": services}
    )