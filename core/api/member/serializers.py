from rest_framework import serializers
from members.models import Member
from managements.models import Executive
from api.loans.serializers import LoanSerializers
from api.auth.serializers import UserSerializers


class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    position = ExecutiveSerializer(read_only=True)
    avaliable_balance = serializers.SerializerMethodField()
    existing_loan = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = "__all__"

    def get_avaliable_balance(self, obj):
        return obj.total_contribution * 2 - obj.total_loan

    def get_existing_loan(self, obj):
        loan = obj.loan.all()
        serializer = LoanSerializers(loan, many=True)
        return serializer.data


class MemberUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "total_contribution": {"read_only": True},
            "total_loan": {"read_only": True},
        }


class MemberUpdateContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["monthly_contribution"]
