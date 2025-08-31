from django.utils import timezone
from .models import AdminInvite

def validate_admin_token(email, token):
    try:
        invite = AdminInvite.objects.get(email=email, token=token, used=False)
        if invite.expires_at and invite.expires_at < timezone.now():
            return False, "Token expired"
        invite.used = True
        invite.save()
        return True, "Token valid"
    except AdminInvite.DoesNotExist:
        return False, "Invalid token"
