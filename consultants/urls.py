from django.urls import path
from .views import (
        consultant_list, 
        consultant_item,
        consultant_search
    )

app_name = 'consultants'

urlpatterns = [
    path('', consultant_list, name='consultants'),
    path('consultant/<uuid:id>', consultant_item, name='consultant'),
    path('search', consultant_search, name='consultant-search')
]
