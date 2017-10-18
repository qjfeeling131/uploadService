import requests
import json
class authorization:
    
    __httpHeaders={'authorization':''}
    __requestUrl='http://172.16.1.109'

    def __init__(self,header):
        self.__httpHeaders['authorization']=header

    #Send the request to API for validating the current reuqest whether have access.
    def sendRequest(self):
        httpReponse=requests.get(self.__requestUrl+'/api/Authorize',headers=self.__httpHeaders)
        # print(httpReponse.json())
        result=JsonData()
        if(httpReponse.status_code==200):
            result.success=True
            dic=json.loads(httpReponse.text)        
            result.userid=dic['id']
            return result
        else:
            result.success=False
            return result



class JsonData:
    success=True
    userid=''
        