from django.db import models
from django.conf import  settings
from couples.models import Couple

class Prompt(models.Model):
    question = models.CharField(max_length=255)
    date = models.DateField(unique=True)    # One prompt per day

    def __str__(self):
        return f"{self.date}: {self.question}"
    
class PromptResponse(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name='responses')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name='prompt_responses')
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('prompt', 'user')    # User can only answer a specific prompt once
    
    def __str__(self):
        return f"Response by {self.user.email} for {self.prompt.date}"
