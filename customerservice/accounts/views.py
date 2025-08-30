from django.http import JsonResponse
from accounts.decorators import role_required  # assuming you moved it to accounts

@role_required(allowed_roles=["superadmin"])
def superadmin_dashboard(request):
    return JsonResponse({"message": "Welcome to the Superadmin Dashboard"})

@role_required(allowed_roles=["admin"])
def admin_dashboard(request):
    return JsonResponse({"message": "Welcome to the Admin Dashboard"})

@role_required(allowed_roles=["customer"])
def customer_dashboard(request):
    return JsonResponse({"message": "Welcome to the Customer Dashboard"})
