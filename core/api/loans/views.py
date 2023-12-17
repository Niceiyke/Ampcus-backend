from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from loans.models import Loan, LoanRepayment, Comment
from django.shortcuts import get_object_or_404

from .serializers import LoanSerializers, LoanRepaymentSerializers, CommentSerializer


class ListCreateLoanView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializers


class LoanDetailapprovedView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializers


class LoanDetailunapprovedView(generics.RetrieveUpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializers


class ListCreateLoanRepaymentView(generics.ListCreateAPIView):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializers


class LoanCommentViews(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserLoanDecline(APIView):
    def post(self, request, pk):
        loan = Loan.objects.filter(id=pk).first()

        loan.is_user_declined = True

        loan.save()

        return Response(
            {
                "status": "Loan Declined by user",
                "status": status.HTTP_200_OK,
            }
        )
