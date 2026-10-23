from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Observation, User

admin.site.site_header = 'Git Laboratory Administration'
admin.site.site_title = 'Laboratory admin'
admin.site.index_title = 'Learners and Git practice records'

@admin.register(User)
class LabUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Academic details', {'fields': ('roll_number',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('Academic details', {'fields': ('email', 'roll_number')}),)

@admin.action(description='Clear notes on selected observations')
def clear_notes(modeladmin, request, queryset):
    queryset.update(notes='')

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'value', 'created_at')
    list_filter = ('created_at', 'owner')
    search_fields = ('title', 'notes', 'owner__username')
    actions = (clear_notes,)
