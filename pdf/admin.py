from django.contrib import admin
from .models import RegisterModel

# Register your models here.

@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']