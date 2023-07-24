from django.contrib import admin
from .models import Rating, Booking, Tour, Image
# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("user", "tour", "rating", "content", "create_time")
    fields = [("user"), ("tour"), ("rating"), ("content")]

@admin.register(Booking)
class BookingAmin(admin.ModelAdmin):
    list_display = ( "user", "tour", "status", "created_at","price","number_of_people","departure_date")
    fields = [ ("user"), ("tour"), ("status")]

@admin.register(Tour)
class TourAmin(admin.ModelAdmin):
    list_display = ( "name", "description", "price", "date",)
    fields = [ ("name"), ("description"), ("price"),("date"),]
    