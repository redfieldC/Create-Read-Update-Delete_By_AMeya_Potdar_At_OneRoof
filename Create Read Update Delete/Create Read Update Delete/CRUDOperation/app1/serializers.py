from .models import EmpModel
from rest_framework import serializers


class CRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpModel
        fields = "__all__"

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpModel
        fields = ['isactive']

        