from django.contrib import admin

# Register your models here.
from webapp.models import Poll, Choice


class PollsAdmin(admin.ModelAdmin):
    list_display = ['question']


admin.site.register(Poll, PollsAdmin)


class ChoicesAdmin(admin.ModelAdmin):
    list_display = ['text']


admin.site.register(Choice, ChoicesAdmin)
