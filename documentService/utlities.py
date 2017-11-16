
import requests
import json


class Authorization:
    
    __httpHeaders={'authorization':''}
    __requestUrl='http://172.16.1.109'

    def __init__(self,header):
        self.__httpHeaders['authorization']=header

    #Send the request to API for validating the current reuqest whether have access.
    def sendRequest(self):
        httpReponse=requests.get(self.__requestUrl+'/api/Authorize',headers=self.__httpHeaders)
        # print(httpReponse.json())
        if(httpReponse.status_code==200):
            dic=json.loads(httpReponse.text)        
            return dic
        else:
            return None
        