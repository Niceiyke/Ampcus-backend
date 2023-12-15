from rest_framework import serializers
from rest_framework import status
from accounts.models import CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token["email"] = user.email
        token["id"] = f"{ user.id}"
        token["member"] = f"{user.member.id}"

        return token


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "sap_number",
            "password",
            "place_of_birth",
            "state_of_origin",
            "lga",
            "marital_status",
            "next_of_kin",
            "phone_number",
            "date_joined_nb",
            "date_of_birth",
            "currnent_grade",
            'member',
        ]
        # fields ='__all__'
        extra_kwargs = {"password": {"write_only": True}}
        extra_kwargs = {"executives": {"read_only": True}}
        extra_kwargs = {"member": {"read_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        if user:
            user.set_password(validated_data["password"])
            user.save()
            # AuditLog.objects.create(user=red, action=f"new user {user.email} created")
            return user
        return {"message": "User not created"}
