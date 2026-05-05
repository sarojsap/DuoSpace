import string
import random
from django.db import models
from django.conf import settings

def generate_invite_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits,k=6))

class InviteCode(models.Model):
    code = models.CharField(max_length=6, unique=True, default=generate_invite_code)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)
    created_by = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Code {self.code} by {self.created_by.email}"
    
class Couple(models.Model):
    user1 = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='couple_user1')
    user2 = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='couple_user2')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Couple: {self.user1.email} & {self.user2.email}"