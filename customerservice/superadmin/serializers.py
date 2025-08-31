from rest_framework import serializers
from .models import AdminInvite

class AdminInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminInvite
        fields = ['email']

class ValidateTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(max_length=12)
