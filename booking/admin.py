from django.contrib import admin
from .models import Service, Worker, Booking, Review, Bill


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'phone',
        'service',
        'worker',
        'date',
        'time_slot',
        'status'
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating', 'comment')


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'created_at')