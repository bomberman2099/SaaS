import helpers.billing
from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
        if not self.stripe_id:

            email = self.user.email
            if email != "" or email is not None:
                stripe_id = helpers.billing.create_customer(email=email, raw=True)
                self.stripe_id = stripe_id

        super().save(*args, **kwargs)
