from django.contrib import admin

from .models import Contact , Booking2

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
   list_display = ('id', 'Name', 'Email', 'Phone')
   list_display_links = ('id', 'Name')
   search_fields = ('Name', 'Email', 'Phone')
   list_per_page = 10

class BookingAdmin2(admin.ModelAdmin):
   list_display = ('Name', 'phone_Number', 'email', 'cab', 'Text')
   search_fields = ('Name', 'phone_Number', 'email', 'cab')
   list_filter = ('Name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Booking2, BookingAdmin2)