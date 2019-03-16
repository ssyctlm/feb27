from django.urls import path
from .views import (
    index_view,
    about_view,
    services_view,
    contact_view
)

# app_name = 'articles'
urlpatterns = [
    path('',index_view,name='home'),
    path('about',about_view,name = 'about'),
    path('services',services_view,name = 'services'),
    path('contact',contact_view,name = 'contact'),
]
