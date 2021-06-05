from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    fields = ('user', 'date', 'duration', 'distance')
    list_filter = ('user', ('date', DateFieldListFilter),)
