from django.urls import path

from pages.views import *
from products.views import *
from blog.views import *
# from . import views
urlpatterns = [
    # App products
    path('', plist),
    path('create/', product_create_view),
    path('<int:p_id>/', dynamic_lookup_view)
]
