from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/superadmin/', include('superadmin.urls')),
    path('api/staff/', include('staff.urls')),

]
