from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Memory
from .serializers import MemorySerializer
from couples.utils import get_user_couple

class MemoryListCreateView(generics.ListCreateAPIView):
    serializer_class = MemorySerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        couple = get_user_couple(self.request.user)
        if couple:
            return Memory.objects.filter(couple=couple)
        return Memory.objects.none()
    
    def perform_create(self, serializer):
        couple = get_user_couple(self.request.user)
        serializer.save(couple=couple)