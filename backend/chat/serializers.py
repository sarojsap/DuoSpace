from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'image', 'timestamp', 'seen']
        read_only_fields = ['sender', 'timestamp', 'seen']