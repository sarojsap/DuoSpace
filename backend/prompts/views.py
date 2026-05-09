from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Prompt, PromptResponse
from .serializers import PromptSerializer, PromptResponseSerializer
from couples.utils import get_user_couple

class DailyPromptView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.now().date()
        # Get today's prompt, or create a fallback one for testing
        prompt, _ = Prompt.objects.get_or_create(
            date=today,
            defaults={'question': 'What made you smile today?'}
        )
        
        couple = get_user_couple(request.user)
        responses = PromptResponse.objects.filter(prompt=prompt, couple=couple)
        
        data = PromptSerializer(prompt).data
        data['responses'] = PromptResponseSerializer(responses, many=True).data
        return Response(data)

    def post(self, request):
        today = timezone.now().date()
        prompt = Prompt.objects.get(date=today)
        couple = get_user_couple(request.user)
        
        # Check if user already answered
        if PromptResponse.objects.filter(prompt=prompt, user=request.user).exists():
            return Response({"error": "Already answered today."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PromptResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(prompt=prompt, user=request.user, couple=couple)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)