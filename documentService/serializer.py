from rest_framework import serializers
from documentService.models import DigitalAsset


class DigitalAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model=DigitalAsset
        fields=('id','name','created','path','createById')



         