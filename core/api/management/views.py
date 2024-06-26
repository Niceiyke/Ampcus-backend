from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from loans.models import Loan,LoanApprovalQueue
from transaction.models import Transaction
from managements.models import Executive
from members.models import Member
from api.loans.serializers import LoanSerializers
from api.auth.serializers import UserSerializers

from .serializes import LoanApprovalSerializers


class LoanDetailView(APIView):
    def get(self, request, pk):
        loan = get_object_or_404(Loan, pk=pk)
        amount = loan.borrowed_amount
        owner = loan.member
        loan_type = loan.loan_type.name
        tresurer_approved = loan.is_tresurer_approved
        president_approved = loan.is_president_approved
        petron_approved = loan.is_petron_approved

        data = {
            "owner": owner,
            "loan_type": loan_type,
            "requested_loan_amount": amount,
            "tresurer_approved": tresurer_approved,
            "president_approved": president_approved,
            "petron_approved": petron_approved,
        }

        serializer = LoanApprovalSerializers(data)

        return Response(serializer.data)


class ListAllActiveLoans(generics.ListAPIView):
    queryset = Loan.objects.filter(is_active=True)
    serializer_class = LoanSerializers


class ApproversView(APIView):
    def get(self, request):
        qs = Executive.objects.filter(
            portfolio="135fac87-72b1-4526-81d2-2932fe3267b7"
        ).first()

        serializer = UserSerializers(qs.name)

        qsp = Member.objects.filter(id=serializer.data["member"]).first()

        qst = Executive.objects.filter(
            portfolio="3d84dcb8-cacb-417b-9336-9bcf10044db4"
        ).first()


        serializert = UserSerializers(qst.name)

        qstp = Member.objects.filter(id=serializert.data["member"]).first()

        return Response(
            {
                "president_id": serializer.data["id"],
                "president_name": f"{serializer.data['first_name']} {serializer.data['last_name'] }",
                "president_email": serializer.data["email"],
                "president_phone": serializer.data["phone_number"],
                "president_picture": str(qsp.profile_picture),

                "treasurer_id": serializert.data["id"],
                "treasurer_name": f"{serializert.data['first_name']} {serializert.data['last_name'] }",
                "treasurer_email": serializert.data["email"],
                "treasurer_phone": serializert.data["phone_number"],
                "treasurer_picture": str(qstp.profile_picture),
            }
        )


class LoansAwaitingApprovals(APIView):
    def get(self,request):

        queryset =LoanApprovalQueue.objects.all()
        queryset =[qs for qs in queryset] 

    
        queryset1 = [Loan.objects.filter(approvalqueue=qs).first() for qs in queryset]

  

        serializer =LoanSerializers(queryset1,many=True)


        print(queryset)
        return Response(
            {
                "loans_awaiting_approvals":serializer.data,
             
            }
        )


class AccountBalances(APIView):
    def get(self, request):
        all_contribution = Transaction.objects.filter(transaction_type=1)
        all_contribution = sum([entry.amount for entry in all_contribution])

        active_loan_balance = Loan.objects.filter(is_active=True)
        active_loan_balance = sum([entry.amount for entry in active_loan_balance])

        return Response(
            {
                "all_contribution": all_contribution,
                "active_loan_balance": active_loan_balance,
            }
        )


@api_view(["POST"])
def send_Executive_Mail(request):
    queryset = Executive.objects.all()
    exco_mail_list = [entry.name.email for entry in queryset]

    subject = request.data["subject"]
    message = request.data["message"]
    from_email = request.data["from"]
    recipient_list = exco_mail_list

    send_mail(subject, message, from_email, recipient_list)

    return Response(
        {
            "message": f"{len(exco_mail_list)} mails sent succeffully",
            "status": status.HTTP_200_OK,
        }
    )


@api_view(["POST"])
def send_Members_Mail(request):
    queryset = Member.objects.all()
    exco_mail_list = [entry.user.email for entry in queryset]

    subject = request.data["subject"]
    message = request.data["message"]
    from_email = request.data["from"]
    recipient_list = exco_mail_list

    send_mail(subject, message, from_email, recipient_list)

    return Response(
        {
            "message": f"{len(exco_mail_list)} mails sent succeffully",
            "status": status.HTTP_200_OK,
        }
    )


@api_view(["POST"])
def send_Personal_mail(request):
    subject = request.data["subject"]
    message = request.data["message"]
    from_email = request.data["from"]
    to_email = request.data["to"]
    send_mail(subject, message, from_email, to_email)

    return Response({"message": "mail sent succeffully", "status": status.HTTP_200_OK})
