
from django.contrib import admin
from django.urls import path


from auth_app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('dashboard/',dashboard_view,name='dashboard'),
]
