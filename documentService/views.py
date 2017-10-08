# from django.shortcuts import render
from documentService.models import DigitalAsset, DigitalAssetManager
from documentService.serializer import DigitalAssetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser
import os, sys
# Create your views here.


class UploadFile(APIView):
    parser_classes=(FileUploadParser, )

    def post(self,request,format=None):
        # file_obj=request.data['file']
        file_obj=request.FILES['file']
        #get the current folder.
        folder=os.getcwd();
        print("the current folder is:"+folder)
        destination=open(folder+'/'+file_obj.name,'wb+')
        for chunk in file_obj.chunks():
            destination.write(chunk)
            destination.close()
        digitalasset=DigitalAsset.objects.create_digitalAsset(file_obj.name,folder+'/'+file_obj.name,"test")
        digitalSerializer=DigitalAssetSerializer(data=digitalasset)
        if digitalSerializer.is_valid():
            digitalSerializer.save()
            return Response(digitalSerializer.data,status=status.HTTP_201_CREATED)
        return Response(file_obj.name,status=status.HTTP_400_BAD_REQUEST)
        #save the file information to db.

        #save the file into local.

class getDocumentInformation(APIView):
    
    def get(self,request,format=None):
        digitalAssets=DigitalAsset.objects.all()
        serializer=DigitalAssetSerializer(digitalAssets,many=True)
        return Response(serializer.data)