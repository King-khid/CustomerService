import random
import string
from django.utils import timezone
from datetime import timedelta
from .models import AdminInvite

def generate_admin_token():
    prefix = "ADM"
    length = 9
    characters = string.ascii_uppercase + string.digits
    random_chars = ''.join(random.choices(characters, k=length))
    return prefix + random_chars

def create_admin_invite(email):
    token = generate_admin_token()
    invite = AdminInvite.objects.create(
        email=email,
        token=token,
        expires_at=timezone.now() + timedelta(days=3)
    )
    return invite
