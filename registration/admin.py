from django.contrib import admin

from registration.models import Participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'email', 'preferred_course_start')
    search_fields = ('surname', 'first_name', 'user__last_name')
    list_filter = ('preferred_course_start', )


admin.site.register(Participant, ParticipantAdmin)
