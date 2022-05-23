from django.contrib import admin

from .models import Organization


# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     list_filter = ['type']

    # exclude = ['created', 'updated']
    
    # fieldsets = (
    #     ('Contact details', {
    #         'fields': ('fullname', 'phone', 'email', 'type', 'image'),
    #         'description': 'Brief personal information about the consultant'
    #     }),
    #     ('Background', {
    #         'fields': ('experience', 'education', 'sphere', 'occupation'),
    #         'description': 'Background information on education and previous/current professional experience'
    #     }),
    #     ('Misc', {
    #         'fields': ('competences', 'languages', 'verified'),
    #         'description': 'Further infomration that is required for hiring the consultant'
    #     }),
    # )