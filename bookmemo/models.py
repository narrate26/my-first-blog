from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core import validators


class Post(models.Model):
    isbn = models.TextField(max_length=13,blank=True, null=True)
    title = models.CharField(max_length=300)
    auther = models.TextField(max_length=100,blank=True, null=True)
    publisher = models.TextField(max_length=100,blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    impression = models.TextField(blank=True, null=True)
    evaluation = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)],blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title