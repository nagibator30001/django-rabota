from django.contrib import admin
from apps.reseptions.models import Recipe
# Register your models here.

@admin.register(Recipe)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name','ingredients','instructions','prep_time','is_vegetarian','created_at']