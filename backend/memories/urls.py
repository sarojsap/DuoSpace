from django.urls import path
from .views import MemoryListCreateView

urlpatterns = [
    path('', MemoryListCreateView.as_view(), name='memory_list'),
]