from django.urls import path
from .views import GenerateInviteView, JoinCoupleView

urlpatterns = [
    path('invite/', GenerateInviteView.as_view(), name='generate_invite'),
    path('join/', JoinCoupleView.as_view(), name='join_couple'),
]