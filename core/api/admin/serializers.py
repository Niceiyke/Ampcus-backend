from rest_framework import serializers

from accounts.models import CustomUser
from members.models import Member


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "sap_number"]


class MemberSerializer(serializers.ModelSerializer):
    user = AdminUserSerializer(read_only=True)

    class Meta:
        model = Member
        fields = "__all__"
