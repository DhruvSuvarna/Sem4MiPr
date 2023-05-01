from django.contrib import admin
from .models import UtilityDonation, ServiceDonation, DonorProfile

# Register your models here.
admin.site.register(DonorProfile)
admin.site.register(UtilityDonation)
admin.site.register(ServiceDonation)
