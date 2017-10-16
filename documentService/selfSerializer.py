from rest_framework import serializers

class restResult(object):
    
    def __init__(self,code,data,message):
        self.code=code
        self.data=data
        self.message=message

class restResultSerializer(serializers.Serializer):
    code=serializers.IntegerField()
    data=serializers.CharField()
    message=serializers.CharField(max_length=500)


result=restResult(101,'test','test')
serializer=restResultSerializer(result)
serializer.data

# class restResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=restResult
#         fields=('code','data','message')

