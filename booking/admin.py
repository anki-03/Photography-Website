from django.contrib import admin

from .models import Booking
# Register your models here.

#@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('Name', 'phone_Number', 'email', 'cab', 'Text')
    search_fields = ('Name', 'phone_Number', 'email', 'cab')
    list_filter = ('Name', 'email')

admin.site.register(Booking, BookingAdmin)
