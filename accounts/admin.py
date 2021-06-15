from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserChangeForm, CustomUserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['image','username','email','age','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age','image')}),
    )

    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age','image')}),
    )

    readonly_fields = ('image')

admin.site.register(CustomUser, UserAdmin)