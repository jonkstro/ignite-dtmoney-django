from rest_framework import viewsets
from transaction.api.serializers import TransactionSerializer

from transaction.models import Transaction


class TransactionViewSet (viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        return Transaction.objects.all()