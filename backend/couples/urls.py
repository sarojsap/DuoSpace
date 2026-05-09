from django.urls import path
from .views import GenerateInviteView, JoinCoupleView, MoodUpdateView

urlpatterns = [
    path('invite/', GenerateInviteView.as_view(), name='generate_invite'),
    path('join/', JoinCoupleView.as_view(), name='join_couple'),
    path('mood/', MoodUpdateView.as_view(), name='update_mood'),
]