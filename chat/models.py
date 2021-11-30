from django.db import models
from datetime import datetime
# from .views import ls
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField


# Create your models here.
class ConvoChats(models.Model):
    message = JSONField(default=list,null=True,blank=True)
    phone = models.CharField(max_length=200, blank=True) 
    contact_date = models.DateTimeField(default=timezone.now(), blank=True)
    def __str__(self):
        return self.phone