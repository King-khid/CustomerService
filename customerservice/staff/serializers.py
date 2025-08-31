from rest_framework import serializers
from django.conf import settings
from django.utils import timezone
from .models import AdminProfile
from superadmin.models import AdminInvite

class AdminRegistrationSerializer(serializers.Serializer):
    token = serializers.CharField()
    company_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    address1 = serializers.CharField(max_length=255)
    address2 = serializers.CharField(max_length=255, required=False, allow_blank=True)
    region = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        try:
            invite = AdminInvite.objects.get(token=data['token'], used=False)
        except AdminInvite.DoesNotExist:
            raise serializers.ValidationError({"token": "Invalid or used token."})

        if invite.expires_at < timezone.now():
            raise serializers.ValidationError({"token": "Token has expired."})

        from django.contrib.auth import get_user_model
        User = get_user_model()
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists."})

        data['invite'] = invite
        return data

    def create(self, validated_data):
        invite = validated_data.pop('invite')
        CustomUser = settings.AUTH_USER_MODEL

        from django.apps import apps
        UserModel = apps.get_model(CustomUser)

        user = UserModel.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            is_staff=True
        )

        AdminProfile.objects.create(
            user=user,
            company_name=validated_data['company_name'],
            address1=validated_data['address1'],
            address2=validated_data.get('address2', ''),
            region=validated_data['region'],
            country=validated_data['country'],
            phone=validated_data['phone']
        )

        invite.is_used = True
        invite.save()
        return user
