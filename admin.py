from django.contrib import admin
from .models import UserProfile, Transaction

# Simple model registrations
admin.site.register(UserProfile)
admin.site.register(Transaction)
