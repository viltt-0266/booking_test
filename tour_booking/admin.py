# admin.py
from django.contrib import admin
from .models import Tour, Booking, Image, Rating

class ImageInline(admin.TabularInline):
    model = Image

class TourAmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date')
    search_fields = ('name',)
    list_filter = ('date',)
    inlines = [ImageInline]

admin.site.register(Tour, TourAmin)

class BookingAmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'status', 'created_at', 'departure_date')
    list_filter = ('status', 'created_at', 'departure_date')
    actions = ['approve_booking', 'reject_booking']

    def approve_booking(self, request, queryset):
        queryset.update(status='Approved')
        # Gửi email cho user khi đơn đặt tour được chấp nhận

    def reject_booking(self, request, queryset):
        queryset.update(status='Rejected')
        # Gửi email cho user khi đơn đặt tour bị từ chối

    approve_booking.short_description = "Phê duyệt đơn đặt Tour"
    reject_booking.short_description = "Từ chối đơn đặt Tour"

admin.site.register(Booking, BookingAmin)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        "rating",
    )

    def has_add_permission(self, request):
        # Vô hiệu hóa khả năng thêm mới người dùng trong trang quản trị
        return False
