from rest_framework import serializers
from documentService.models import DigitalAsset


class DigitalAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model=DigitalAsset
        fields=('id','name','createTime','path','createByUserId')


class ResetResultSerializer(serializers.Serializer):
    code=serializers.IntegerField()
    data=serializers.CharField()
    message=serializers.CharField(max_length=500)