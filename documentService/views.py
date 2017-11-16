from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser
from django.http import HttpResponse
from wsgiref.util import FileWrapper

import os, sys
import requests
import uuid
import logging
import shutil
import time

from documentService.models import DigitalAsset,RestResult
from documentService.serializers import DigitalAssetSerializer,ResetResultSerializer
from documentService.utlities import Authorization
# Create your views here.
class HandleFiles(APIView):
    parser_classes=(FileUploadParser,JSONParser )
    _restReult=RestResult(102,'','Upload failed')
    logging.basicConfig(filename='handle files.log',format='%(levelname)s:%(asctime)s %(message)s',level=logging.DEBUG)

    def createFolder(self,currentFoler,folderName):
        #TODO:Check the current foleer whether exist
        newFoler=currentFoler+"/"+folderName
        folderIsExisted=os.path.exists(newFoler)
        if folderIsExisted!=True:
            os.mkdir(newFoler)
            return newFoler
        return newFoler

    def post(self,request,format=None):
        tokenHeader=request.META['HTTP_AUTHORIZATION']
        authorize=Authorization(tokenHeader)
        result= authorize.sendRequest()
        if result is None:
            logging.warning("The current user have not access to call upload file feature")
            self._restReult.message='The current user have not access to call upload file feature'
            resultSErializer=ResetResultSerializer(self._restReult)
            return Response(resultSErializer.data,status=status.HTTP_400_BAD_REQUEST)       
        file_obj=request.FILES['file']
        #get the current folder.
        folder=os.getcwd();
        contentType=''
        path=''
        size=0.00
        fileNameList=file_obj.name.split('.')
        fileNameListCount=len(fileNameList)
        if fileNameListCount<2:
            logging.error("The file name is invalid")
            self._restReult.message='The file name is invalid'
            resultSErializer=ResetResultSerializer(self._restReult)
            return Response(resultSErializer.data,status.HTTP_400_BAD_REQUEST)
        contentType=fileNameList[fileNameListCount-1]       
        #TODO:Get file name
        fileName=''
        digitalId=str(uuid.uuid4())
        index=0
        while index<fileNameListCount-1:
            fileName=fileName+fileNameList[index]
            index+=1
        userFoler=self.createFolder(folder, result['id'])
        digitalassetFolder=self.createFolder(userFoler,digitalId)
        path=digitalassetFolder+'/'+file_obj.name
        try:
            destination=open(path,'wb+')
            for chunk in file_obj.chunks():
                destination.write(chunk)
                size+=len(chunk)
            destination.close()
            size=size/1024
            #TODO:Create digitalAsset object
            asset=DigitalAsset(digitalId,fileName,contentType,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),result['id'],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),result['id'],path,size,'')
            asset.save()
            assetSerializer=DigitalAssetSerializer(asset)
            return Response(assetSerializer.data,status=status.HTTP_201_CREATED)          
        except Exception as ex:
            logging.error(ex)
            self._restReult.message="Application occurs some error, please contact the Admin to check."
            self._restReult.code=104
            resultSerializer=ResetResultSerializer(self._restReult)
            shutil.rmtree(digitalassetFolder)
            return Response(resultSerializer.data,status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return DigitalAsset.objects.get(pk=pk)
        except DigitalAsset.DoesNotExist:
            raise Http404

    def get(self,request,format=None):
        try:
            tokenHeader=request.META['HTTP_AUTHORIZATION']
            digitalAssetId=request.query_params.get('id')
            authorize=Authorization(tokenHeader)
            result= authorize.sendRequest()
            if result is None:
                logging.warning("The current user have not access to call upload file feature")
                self._restReult.message='The current user have not access to call upload file feature'
                resultSErializer=ResetResultSerializer(self._restReult)
                return Response(resultSErializer.data,status=status.HTTP_400_BAD_REQUEST)       
            digitalasset=self.get_object(digitalAssetId)
            file=open(digitalasset.path,'rb')
            response=HttpResponse(FileWrapper(file), content_type='APPLICATION/OCTET-STREAM')
            response['Content-Disposition']='attachment;filename='+digitalasset.name+'.'+digitalasset.contentType
            response['Content-Length']=os.path.getsize(digitalasset.path)
            return response
        except Exception as e:
            logging.error(e)
            self._restReult.message="The digital asset Id is incorrect, please check your digital id"
            resultSerializer=ResetResultSerializer(self._restReult)
            return Response(resultSerializer.data,status=HTTP_400_BAD_REQUEST)