from django.utils import timezone
from django.db import models

import uuid

class survey(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  json = models.JSONField()

  code = models.CharField(max_length=100, null=True, blank=True, unique=True)

  is_anonymous = models.BooleanField(default=False)

  limit = models.IntegerField(default=5)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()

  created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  @property
  def is_enough(self):
    return respondent.objects.filter(survey=self).count() >= self.limit

  @property
  def is_active(self):
    return self.start_time <= timezone.now() <= self.end_time

  def __str__(self):
    return self.title

  # def save(self, *args, **kwargs):
  #   if not self.code:
  #     self.code = uuid.uuid4().hex
  #   super().save(*args, **kwargs)

class respondent(models.Model):
  survey = models.ForeignKey(survey, on_delete=models.CASCADE)
  bio = models.JSONField()
  location = models.TextField(blank=True, null=True)
  latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
  answer = models.JSONField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.bio.get('name', '')