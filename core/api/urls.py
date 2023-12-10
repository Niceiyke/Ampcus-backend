from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .auth import views as authviews
from .member import views as memberviews
from .transaction import views as transactionviews
from .loans import views as loanviews
from .management import views as managementvies
from .admin import views as adminviews

urlpatterns = [
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("signup/", authviews.RegisterUserView.as_view()),
    path("login/", authviews.LoginUserView.as_view()),
    path("user/", authviews.UserView.as_view()),
    # members urls
    path("member/<str:pk>", memberviews.MemberView.as_view()),
    path("member-update/<str:pk>", memberviews.MemberUpdate.as_view()),
    path(
        "member-contribution/<str:pk>", memberviews.MemberUpdateContribution.as_view()
    ),
    # Transaction Urls
    path("transaction/", transactionviews.ListCreateTransaction.as_view()),
    # Loan Urls
    path("loans/", loanviews.ListCreateLoanView.as_view()),
    path("loan-detail-approved/<str:pk>", loanviews.LoanDetailapprovedView.as_view()),
    path(
        "loan-detail-unapproved/<str:pk>", loanviews.LoanDetailunapprovedView.as_view()
    ),
    path("loan-repayment/", loanviews.ListCreateLoanRepaymentView.as_view()),
    path("approve-loan/<str:pk>/", loanviews.LoanApprovalAPIView.as_view()),
    # Managementsurls
    path("loan-detail/<str:pk>/", managementvies.LoanDetailView.as_view()),
    path("all-contribution/", managementvies.AccountBalances.as_view()),
    path("send-exco-mail/", managementvies.send_Executive_Mail),
    path("send-members-mail/", managementvies.send_Members_Mail),
    path("send-personal-mail/", managementvies.send_Personal_mail),
    # Admin
    path("admin/list-users", adminviews.ListAllUsersView.as_view()),
    path("admin/list-members", adminviews.ListAllMembersView.as_view()),
    path("admin/user/<str:pk>", adminviews.RUDUsersView.as_view()),
    path("admin/member/<str:pk>", adminviews.RUDMembersView.as_view()),
]
