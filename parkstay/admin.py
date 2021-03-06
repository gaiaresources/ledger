from django.contrib import messages
from django.contrib import admin
from parkstay import models 

@admin.register(models.CampsiteClass)
class CampsiteClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(models.Park)
class ParkAdmin(admin.ModelAdmin):
    list_display = ('name','district')
    ordering = ('name',)
    list_filter = ('district',)
    search_fields = ('name',)

@admin.register(models.Campground)
class CampgroundAdmin(admin.ModelAdmin):
    list_display = ('name','park','promo_area','campground_type','site_type')
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('campground_type','site_type')

@admin.register(models.Campsite)
class CampsiteAdmin(admin.ModelAdmin):
    list_display = ('name','campground',)
    ordering = ('name',)
    list_filter = ('campground',)
    search_fields = ('name',)

@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('arrival','departure','campground','legacy_id','legacy_name','cost_total')
    ordering = ('-arrival',)
    search_fileds = ('arrival','departure')
    list_filter = ('arrival','departure')

@admin.register(models.CampsiteBooking)
class CampsiteBookingAdmin(admin.ModelAdmin):
    list_display = ('campsite','date','booking','booking_type')
    ordering = ('-date',)
    search_fields = ('date',)
    list_filter = ('campsite','booking_type')

@admin.register(models.CampsiteRate)
class CampsiteRateAdmin(admin.ModelAdmin):
    list_display = ('campsite','rate','allow_public_holidays')
    list_filter = ('campsite','rate','allow_public_holidays')
    search_fields = ('campground__name',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number')
    search_fields = ('name','phone_number')

class ReasonAdmin(admin.ModelAdmin):
    list_display = ('code','text','editable')
    search_fields = ('code','text')
    readonly_fields = ('code',)

    def get_readonly_fields(self, request, obj=None):
        fields = list(self.readonly_fields)
        if obj and not obj.editable:
            fields += ['text','editable']
        elif not obj:
            fields = []
        return fields

    def has_add_permission(self, request, obj=None):
        if obj and not obj.editable:
            return False
        return super(ReasonAdmin, self).has_delete_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and not obj.editable:
            return False
        return super(ReasonAdmin, self).has_delete_permission(request, obj)

@admin.register(models.MaximumStayReason)
class MaximumStayReason(ReasonAdmin):
    pass

@admin.register(models.PriceReason)
class PriceReason(ReasonAdmin):
    pass

@admin.register(models.ClosureReason)
class ClosureReason(ReasonAdmin):
    pass

@admin.register(models.OpenReason)
class OpenReason(ReasonAdmin):
    pass

admin.site.register(models.Rate)
admin.site.register(models.Region)
admin.site.register(models.District)
admin.site.register(models.PromoArea)

