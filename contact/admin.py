from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone']
    ordering = ['first_name']
    list_filter = 'created_data', 'category',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']