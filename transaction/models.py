from django.db import models


class Transaction (models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type_transaction = models.CharField(max_length=10, null=False, blank=False)
    category = models.CharField(max_length=255, null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title