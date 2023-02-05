from django.contrib import admin
from .models import Event,Extra,Contact
from . import models
from . import forms

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    form = forms.EventAdminForm

class ExtraAdmin(admin.ModelAdmin):
    form = forms.ExtraAdminForm

admin.site.register(Event,EventAdmin)
admin.site.register(Extra,ExtraAdmin)
admin.site.register(Contact)