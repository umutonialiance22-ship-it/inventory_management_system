from rest_framework import serializers
from .models import Supplier
class SupplierSerializer(serializers.ModelSserializer):
    class Meta:
        model=Supplier
        field='__all__'
        