from django.contrib import admin
from .models import *
# Register your models here.
@admin.register((mission))
class missionModelAdmin(admin.ModelAdmin):
    list_display = ['id','mission_title','mission_completed']