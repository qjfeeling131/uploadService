from django.db import models

# Create your models here.

class DigitalAssetManager(models.Manager):
    def create_digitalAsset(self,name,path,createById):
        digitalasset=self.create(name=name,path=path,createById=createById)
        return digitalasset
        
    

class DigitalAsset(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=50,blank=True,default='')
    path=models.CharField(max_length=200,blank=True,default='')
    createById=models.CharField(max_length=36,blank=True,default='')

    objects=DigitalAssetManager()
    class Meta:
        ordering=('created',)

