from django.db import models
from django.conf import settings


class Group(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='led_groups'
    )

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='joined_groups'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name