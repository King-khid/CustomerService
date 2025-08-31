from django.urls import path
from .views import CreateAdminInviteView, ValidateTokenView

urlpatterns = [
    path('invite/', CreateAdminInviteView.as_view(), name='create-admin-invite'),
    path('validate-token/', ValidateTokenView.as_view(), name='validate-admin-token'),
]
