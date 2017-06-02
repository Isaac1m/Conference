from django.contrib import admin
from .models import *


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio',)
    fieldsets = (

        ('General Information', {
            'fields': ('name', 'bio',)
        }),

        ('Social media', {
            'classes': ('collapse',),
            'fields': ('twitter', 'facebook',),
            'description': 'Add social media here.',
        }),
    )


class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'speaker',)
    search_fields = ('title', 'abstract',)
    list_filter = ('track__title', 'speaker',)
    actions = ['make_approved', ]

    def make_approved(self, request, queryset):
        rows_updated = queryset.update(status='a')
        if rows_updated == 1:
            message_bit = '1 session was '
        else:
            message_bit = '%s sessions were ' % rows_updated
        self.message_user(request, '%s updated.' % message_bit)

    make_approved.short_description = 'Mark session(s) as approved.'


admin.site.register(Track)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Session, SessionAdmin)
