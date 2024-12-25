from django.db import models
from django.contrib.auth.models import Group, Permission
# Create your models here.



SUBSCRIPTION_PERMISSIONS = [
            ("advanced", "Advanced Perm"), # subscriptions.advanced
            ("pro", "Pro Perm"),
            ("basic", "Basic Perm"),
            ("basic_ai", "Basic AI Perm"),
        ]


class Subscription(models.Model):
    name = models.CharField(max_length=120)
    groups = models.ManyToManyField(Group)
    active = models.BooleanField(default=True)
    permissions = models.ManyToManyField(Permission, limit_choices_to={"content_type__app_label": "subscriptions", 'codename__in': [X[0] for X in SUBSCRIPTION_PERMISSIONS]})
    class Meta:
        permissions = SUBSCRIPTION_PERMISSIONS

    def __str__(self):
        return self.name