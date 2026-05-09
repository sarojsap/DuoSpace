from django.urls import path
from .views import DailyPromptView

urlpatterns = [
    path('daily/', DailyPromptView.as_view(), name='daily_prompt'),
]