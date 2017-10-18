from rest_framework import serializers
from documentService.selfModels import restResult,digitalAsset
from documentService.dbHelper import SQLHelper


class digitalAssetSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    contentType=serializers.CharField(max_length=5)
    # createByUserId=serializers.CharField(max_length=36)
    createTime=serializers.DateTimeField()
    # modifyByUserId=serializers.CharField(max_length=36)
    modifyTime=serializers.DateTimeField()
    # path=serializers.CharField()
    size=serializers.IntegerField()
    # extension=serializers.CharField()

    def create(self,validated_data):
        return digitalAsset(**validated_data)

    def update(self,instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.contentType=validated_data.get('contentType',instance.contentType)
        instance.createByUserId=validated_data.get('createByUserId',instance.createByUserId)
        instance.createTime=validated_data.get('createTime',instance.createTime)
        instance.modifyByUserId=validated_data.get('modifyByUserId',instance.modifyByUserId)
        instance.modifyTime=validated_data.get('modifyTime',instance.modifyTime)
        instance.path=validated_data.get('path',instance.path)
        instance.size=validated_data.get('size',instance.size)
        instance.extension=validated_data.get('extension',instance.extension)
        instance.save()
        return instance

    # def save(self):
    #     try:
    #         db=SQLHelper()
    #         db.addDigitalAsset(self)
    #     except Exception as ex:
    #         raise ex
    #     finally:
    #         db.release()




class restResultSerializer(serializers.Serializer):
    code=serializers.IntegerField()
    data=digitalAssetSerializer(required=False)
    message=serializers.CharField(max_length=500)


