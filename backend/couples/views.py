from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import InviteCode, Couple, Mood
from couples.utils import get_user_couple

class GenerateInviteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        # Check if user is already in a couple
        if hasattr(user, 'couple_user1') or hasattr(user, 'couple_user2'):
            return Response({"error":"You are already paired."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Invalidate any old unused codes for this user
        InviteCode.objects.filter(created_by=user, is_used=False).delete()

        # Create new code
        invite = InviteCode.objects.create(created_by=user)
        return Response({"code":invite.code}, status=status.HTTP_201_CREATED)
    
class JoinCoupleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        code = request.data.get('code')

        if hasattr(user, 'couple_user1') or hasattr(user, 'couple_user2'):
            return Response({"error": "You are already paired."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            invite = InviteCode.objects.get(code=code, is_used=False)
        except InviteCode.DoesNotExist:
            return Response({"error": "Invalid or expired code."}, status=status.HTTP_404_NOT_FOUND)
        
        if invite.created_by == user:
            return Response({"error": "You cannot use your own code."}, status=status.HTTP_400_BAD_REQUEST)
        
        # transaction.atomic() ensures both database actions succeed, or neither do
        with transaction.atomic():
            # Create the couple
            couple = Couple.objects.create(user1=invite.created_by, user2=user)
            # Mark code as used
            invite.is_used = True
            invite.save()
        
        return Response({"message": "Successfully paired!", "couple_id": couple.id}, status=status.HTTP_200_OK)
    
class MoodUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        couple = get_user_couple(request.user)
        moods = Mood.objects.filter(couple=couple)
        data = [{"user_id": m.user.id, "emoji": m.emoji, "text": m.text, "updated_at": m.updated_at} for m in moods]
        return Response(data)

    def post(self, request):
        couple = get_user_couple(request.user)
        mood, created = Mood.objects.update_or_create(
            user=request.user,
            couple=couple,
            defaults={'emoji': request.data.get('emoji', '😐'), 'text': request.data.get('text', '')}
        )
        return Response({"message": "Mood updated", "emoji": mood.emoji})