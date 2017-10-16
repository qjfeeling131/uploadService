# from django.shortcuts import render
# from documentService.models import DigitalAsset, DigitalAssetManager
# from documentService.serializer import DigitalAssetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser
from documentService.customValidate import authorization
from documentService.dbHelper import SQLHelper
from documentService.selfModels import digitalAsset
import os, sys
import requests

# Create your views here.


class UploadFile(APIView):
    parser_classes=(FileUploadParser, )

    def post(self,request,format=None):
        # file_obj=request.data['file']
        tokenHeader=request.META['HTTP_AUTHORIZATION']
        authorize=authorization(tokenHeader)
        result= authorize.sendRequest()
        if result.success !=True:
            return Response(status=status.HTTP_400_BAD_REQUEST)       
        file_obj=request.FILES['file']
        #get the current folder.
        folder=os.getcwd();
        #TODO:Create digitalAsset object
        digitalasset=digitalAsset()
        fileNameList=file_obj.name.split('.')
        fileNameListCount=len(fileNameList)
        if fileNameListCount<2:
            return Response("The file name is invalid",status.HTTP_400_BAD_REQUEST)
        digitalasset.contentType=fileNameList[fileNameListCount-1]
        
        #TODO:Get file name
        fileName=''
        index=0
        while index<fileNameListCount-1:
            fileName=fileName+fileNameList[index]
            index+=1
        digitalasset.name=fileName
        digitalasset.createByUserId=result.userid
        digitalasset.path=folder+'\\'+digitalasset.createByUserId+'\\'+file_obj.name
        try:
            destination=open(folder+'\\'+file_obj.name,'wb+')
            for chunk in file_obj.chunks():
                destination.write(chunk)
                digitalasset.size+=len(chunk)
            destination.close()
            digitalasset.size=digitalasset.size/1024
            digitalasset.create()
            return Response(status=status.HTTP_201_CREATED)          
        except Exception as ex:
            print(ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class digitalAssets(APIView):
    parser_classes=(JSONParser,)
    def get(self,request,format=None):
        tokenHeader=request.META['HTTP_AUTHORIZATION']
        authorize=authorization(tokenHeader)
        result= authorize.sendRequest()
        if result !=True:
            return Response(status=status.HTTP_400_BAD_REQUEST)  
        db=SQLHelper()
        result=db.getAllUser()
        db.release();
        return Response(result)
    
    def post(self,request,format=None):
        tokenHeader=request.META['HTTP_AUTHORIZATION']
        authorize=authorization(tokenHeader)
        result= authorize.sendRequest()
        if result !=True:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        print(request.data)

