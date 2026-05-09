from django.db import models
from couples.models import Couple

class Memory(models.Model):
    couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name='memories')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='memory_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Memory for {self.couple} on {self.created_at.date()}"
