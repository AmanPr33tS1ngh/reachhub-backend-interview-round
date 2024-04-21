from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Ingestion(models.Model):
    
    class YearInSchool(models.TextChoices):
        ERROR = 'ERROR', _('Error')
        INFO = 'INFO', _('Info')
        
    timestamp = models.DateTimeField(null=False)
    level = models.CharField(
        max_length=5,
        choices=YearInSchool.choices,
        null=False
    )
    message = models.TextField(null=False,)
    userId = models.IntegerField(null=False,)
    
    def __str__(self) -> str:
        return f"{self.userId} - {self.level} -> {self.message}"
    
    class Meta:
        indexes = [
            models.Index(fields=['level']),
            models.Index(fields=['userId']),
            models.Index(fields=['level', 'userId']),
        ]
