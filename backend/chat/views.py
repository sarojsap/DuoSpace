from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Message
from .serializers import MessageSerializer
from couples.utils import get_user_couple

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]  # Handles image uploads

    def get_queryset(self):
        couple = get_user_couple(self.request.user)
        if couple:
            return Message.objects.filter(couple=couple)
        return Message.objects.none()
    
    def perform_create(self, serializer):
        # Automatically assign the sender and couple securely on the backend
        couple = get_user_couple(self.request.user)
        serializer.save(sender=self.request.user, couple=couple)