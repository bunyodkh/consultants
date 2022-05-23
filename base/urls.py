from django.shortcuts import render, get_list_or_404
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from consultants.admin import consultant_site
from consultants.models import Consultant

def homepage(request):
    consultants = get_list_or_404(Consultant)
    return render(request, 'index.html', { 'cs': consultants })


urlpatterns = [
    path('', homepage, name="index"),
    path('consultants/', include('consultants.urls')),
    path('organizations/', include('organizations.urls')),
    path('admin/', admin.site.urls),
    path('add-consultant/', consultant_site.urls),
    path('summernote/', include('django_summernote.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
