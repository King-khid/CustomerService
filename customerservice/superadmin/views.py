from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdminInviteSerializer, ValidateTokenSerializer
from .utils import create_admin_invite
from .email_service import send_admin_invite_email
from .validators import validate_admin_token
from rest_framework.permissions import IsAdminUser

class CreateAdminInviteView(APIView):
    permission_classes = [IsAdminUser]  # Only superadmin can send invites

    def post(self, request):
        serializer = AdminInviteSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            invite = create_admin_invite(email)
            send_admin_invite_email(email, invite.token)
            return Response({"message": f"Invite sent to {email}"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidateTokenView(APIView):
    def post(self, request):
        serializer = ValidateTokenSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            token = serializer.validated_data['token']
            valid, message = validate_admin_token(email, token)
            if valid:
                return Response({"message": message}, status=status.HTTP_200_OK)
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
