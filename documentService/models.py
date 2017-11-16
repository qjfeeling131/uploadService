from django.db import models
from datetime import datetime

# Create your models here.
class DigitalAsset(models.Model):
    
    id=models.CharField(max_length=36,primary_key=True)
    name=models.CharField(max_length=50,blank=True, default='')
    contentType=models.CharField(max_length=100,blank=True, default='')
    createTime=models.DateTimeField()
    createByUserId=models.CharField(max_length=36)
    modifyTime=models.DateTimeField()
    modifyByUserId=models.CharField(max_length=36)
    path=models.CharField(max_length=1000)
    size=models.FloatField()
    extension=models.CharField(max_length=5000)
    class Meta:
         db_table='mo_digitalasset'

class RestResult(object):
    
    def __init__(self,code,data,message):
        self.code=code
        self.data=data
        self.message=message

