from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdminRegistrationSerializer

class RegisterAdminView(APIView):
    """
    API endpoint for registering an admin using an invitation token.
    """
    def post(self, request):
        serializer = AdminRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Creates the custom user + admin profile + marks token used
            return Response(
                {"message": "Admin registered successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
