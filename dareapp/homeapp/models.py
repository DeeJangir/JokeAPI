from django.db import models
import uuid
# Create your models here.


class DareText(models.Model):
    share_text = models.CharField(default="", max_length=5000)
    share_id = models.UUIDField(default=uuid.uuid4, editable=True)


class JokeText(models.Model):
    joke_text = models.CharField(default="", max_length=5000)
    joke_id = models.UUIDField(default=uuid.uuid4, editable=True)


class QuotesText(models.Model):
    quotes_text = models.CharField(default="", max_length=5000)
    quotes_author = models.CharField(default="", max_length=140)
    quotes_id = models.UUIDField(default=uuid.uuid4, editable=True)
