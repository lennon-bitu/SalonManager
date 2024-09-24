from rest_framework import serializers
from usersPerson.models import ClientTenant


class ClientTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model= ClientTenant
        fields = ['id', 'name']