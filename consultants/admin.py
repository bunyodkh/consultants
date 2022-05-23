from django.contrib import admin
import django.apps
from django_summernote.admin import SummernoteModelAdmin

from .models import Consultant, Language, Sphere, Competence, Occupation
from organizations.models import Organization

class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'age', 'gender', 'occupation', 'display_languages', 'type', 'organization')
    list_filter = ('age', 'gender', 'type', 'occupation', 'organization')

    exclude = ['created', 'updated']
    
    fieldsets = (
        ('Personal and contact details', {
            'fields': ('fullname', 'gender', 'phone', 'email', 'type', 'image'),
            'description': 'Brief personal information about the consultant'
        }),
        ('Background', {
            'fields': ('experience', 'education', 'sphere', 'occupation'),
            'description': 'Background information on education and previous/current professional experience'
        }),
        ('Misc', {
            'fields': ('organization', 'competences', 'languages', 'verified'),
            'description': 'Further infomration that is required for hiring the consultant'
        }),
    )

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['type']


class SummernoteAdmin(ConsultantAdmin, SummernoteModelAdmin):
    summernote_fields = ['experience', 'education']


class ConsultantAdminArea(admin.AdminSite):
    site_header = 'Consultants DB Admin Panel'
    index_title = 'Consultants DB'
    site_title = 'Consultants Administration'

consultant_site = ConsultantAdminArea(name='ConsultantAdmin')


consultant_site.register(Consultant, SummernoteAdmin)
admin.site.register(Consultant, SummernoteAdmin)
admin.site.register(Organization, OrganizationAdmin)


consultant_site.register(Sphere)
consultant_site.register(Competence)
consultant_site.register(Occupation)


models = django.apps.apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.unregister(django.contrib.sessions.models.Session)
admin.site.unregister(Language)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


