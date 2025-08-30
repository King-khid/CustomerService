# from django.shortcuts import redirect
# from django.urls import reverse
#
# class RoleRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         if request.path.startswith("/admin/") and request.user.is_authenticated:
#             if request.user.role != "superadmin":
#                 return redirect(reverse("no_permission"))
#
#         return self.get_response(request)
