from django.contrib import admin
from .models import UtilityDonation, ServiceDonation

# Register your models here.

admin.site.register(UtilityDonation)
admin.site.register(ServiceDonation)