from django.urls import path
from .views import RegisterAdminView
from . import views

urlpatterns = [
    path('register-admin/', RegisterAdminView.as_view(), name='register_admin'),
    path("verify-admin/<uidb64>/<token>/", views.verify_admin, name="verify_admin"),

]

