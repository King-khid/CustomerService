from django.core.mail import send_mail
from django.conf import settings

def send_admin_invite_email(email, token):
    subject = "CustomerService Admin Invitation"

    message = f"""
Dear {email},

You have been invited to join CustomerService as an admin.
Kindly click on the link below to register:

http://127.0.0.1:8000/register-admin/?token={token}

Best regards,
CustomerService Team!
"""

    # Format: "Display Name <actual_email>"
    from_email = f"CustomerService <{settings.EMAIL_HOST_USER}>"

    send_mail(
        subject,
        message,
        from_email,
        [email],
        fail_silently=False,
    )
