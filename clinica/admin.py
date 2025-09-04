from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('reflexo Info', {'fields': ('reflexo',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('reflexo Info', {'fields': ('reflexo',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)