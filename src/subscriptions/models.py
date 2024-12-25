from django.db import models
from django.contrib.auth.models import Group, Permission
# Create your models here.
from django.db.models.signals import post_save
from django.conf import settings

User = settings.AUTH_USER_MODEL

SUBSCRIPTION_PERMISSIONS = [
    ("advanced", "Advanced Perm"),  # subscriptions.advanced
    ("pro", "Pro Perm"),
    ("basic", "Basic Perm"),
    ("basic_ai", "Basic AI Perm"),
]


class Subscription(models.Model):
    name = models.CharField(max_length=120)
    groups = models.ManyToManyField(Group)
    active = models.BooleanField(default=True)
    permissions = models.ManyToManyField(Permission, limit_choices_to={"content_type__app_label": "subscriptions",
                                                                       'codename__in': [X[0] for X in
                                                                                        SUBSCRIPTION_PERMISSIONS]})

    class Meta:
        permissions = SUBSCRIPTION_PERMISSIONS

    def __str__(self):
        return self.name

class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} : {self.subscription}'


def user_sub_post_save(sender, instance,*args, **kwargs):
    user_sub_instance = instance # UserSubscription obj
    user = user_sub_instance.user # obj.user
    subscription_obj = user_sub_instance.subscription
    groups = subscription_obj.groups.all()
    user.groups.set(groups)


post_save.connect(user_sub_post_save, sender=UserSubscription)