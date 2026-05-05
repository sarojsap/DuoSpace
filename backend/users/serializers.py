from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        # Using create_user so the password gets hashed
        user = User.objects.create_user(
            email = validated_data['email'],
            password=validated_data['password']
        )
        return user