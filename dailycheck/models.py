from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    is_completed = models.BooleanField()
    # user = models.ForeignKey(
    #     Profile, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.task
    
