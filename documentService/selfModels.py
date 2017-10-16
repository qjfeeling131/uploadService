import time
import uuid
from documentService.dbHelper import SQLHelper
class digitalAsset:
    
    id=str(uuid.uuid4())
    name=''
    contentType=''
    createTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    createByUserId=''
    modifyTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    modifyByUserId=''
    path=''
    size=0
    extension=''

    def create(self):
        try:
            db=SQLHelper()
            db.addDigitalAsset(self)
        except Exception as ex:
            raise ex
        finally:
            db.release()

    # __init__(self,name,contentType,createByUserId,modifyByUserId,path,size,extension):

    # self.name=name
    # self.contentType=contentType
    # self.createByUserId=createByUserId
    # self.modifyByUserId=modifyByUserId
    # self.path=path
    # self.size=size
    # self.extension=extension

class restResult(object):
    
    def __init__(self,code,data,message):
        self.code=code
        self.data=data
        self.message=message
