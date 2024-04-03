from django.contrib import admin

from .models import Member

    
class MemberAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
            super().save_model(request, obj, form, change)
    
    
    search_fields = ['name', 'search_field', 'intro', 'interests']
    list_display = ['name', 'created_at']
    list_filter = ['created_at']

    
admin.site.register(Member, MemberAdmin)