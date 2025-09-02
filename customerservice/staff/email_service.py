from django.core.mail import send_mail
from django.conf import settings
from .utils import generate_verification_link


def send_verification_email(user):
    verification_link = generate_verification_link(user)

    subject = "Verify Your Admin Account - CustomerService"
    message = f"""
Dear {user.email},

Thank you for registering as an Admin on CustomerService.

Please verify your account by clicking the link below:

{verification_link}

If you did not create this account, please ignore this email.

Best regards,
CustomerService Team!
"""

    from_email = f"CustomerService <{settings.EMAIL_HOST_USER}>"

    send_mail(
        subject,
        message,
        from_email,
        [user.email],
        fail_silently=False,
    )
