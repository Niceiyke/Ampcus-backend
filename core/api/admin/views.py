from rest_framework import generics, status
from members.models import Member

from accounts.models import CustomUser
from .serializers import MemberSerializer, AdminUserSerializer


class ListAllUsersView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserSerializer


class RUDUsersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserSerializer


class ListAllMembersView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class RUDMembersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
