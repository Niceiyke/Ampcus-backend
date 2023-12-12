from rest_framework import serializers
from loans.models import Loan, LoanType, LoanRepayment, HomeAppliance, FoodItem, Comment

from api.services import (
    pay_loan,
    process_loan_transaction,
    check_loan_eligibility,
    update_contribution_amount,
)


class LoanTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoanType
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class LoanSerializers(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    loan_types = serializers.SerializerMethodField()
    comments =CommentSerializer(read_only=True,many=True)

    class Meta:
        model = Loan
        fields = [
            "id",
            "borrowed_amount",
            "repaid_amount",
            "member",
            "loan_type",
            "comments",
            "is_active",
            "is_approved",
            "is_treasurer_approved",
            "is_declined",
            "is_president_approved",
            "is_user_declined",
            "is_treasurer_declined",
            "is_president_declined",
            "owner",
            "is_user_declined",
            "loan_types",
            "date_initiated",
            "date_declined",
            "date_updated",
            "date_approved",
        ]

        extra_kwargs = {
            "repaid_amount": {"read_only": True},
            "is_active": {"read_only": True},
            "is_approved": {"read_only": True},
            "is_declined": {"read_only": True},
        }

    def get_owner(self, obj):
        owner = f"{obj.member.user.first_name} {obj.member.user.last_name}"
        return owner

    def get_loan_types(self, obj):
        type = f"{obj.loan_type.name}"
        return type

    def create(self, validated_data):
        response = check_loan_eligibility(
            member_object=validated_data["member"],
            selected_loan_type=validated_data["loan_type"],
            requested_amount=validated_data["borrowed_amount"],
        )

        if response["status"] == True:
            process_loan_transaction(
                transaction_amount=validated_data["borrowed_amount"],
                member_object=validated_data["member"],
                transaction_type="Debit",
            )
            response = super().create(validated_data)
            response.save()
            return response

        raise serializers.ValidationError(response["error"])


class LoanRepaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoanRepayment
        fields = "__all__"

    def create(self, validated_data):
        response = pay_loan(
            amount=validated_data["borrowed_amount"], loan=validated_data["loan"]
        )

        if response["status"] == 200:
            process_loan_transaction(
                transaction_type="Credit",
                transaction_amount=validated_data["borrowed_amount"],
                member_object=validated_data["loan"].member,
            )
            return super().create(validated_data)

        else:
            raise serializers.ValidationError(response["error"])


class HomeApplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAppliance
        fields = "__all__"


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = "__all__"
