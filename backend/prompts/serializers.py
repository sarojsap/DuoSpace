from rest_framework import serializers
from .models import Prompt, PromptResponse

class PromptResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptResponse
        fields = ['id', 'user', 'answer', 'created_at']
        read_only_fields = ['user']

class PromptSerializer(serializers.ModelSerializer):
    # We will dynamically attach the responses for this couple in the view
    class Meta:
        model = Prompt
        fields = ['id', 'question', 'date']