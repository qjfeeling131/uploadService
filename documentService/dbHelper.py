import pymysql
import uuid
#We should make this helper to more smart, it will optimize this bolock in next Sprint!!!!
class SQLHelper():
    
    config={
        'host':'127.0.0.1',
        'port':3306,
        'user':'root',
        'db':'mimeooa',
        'password':'123456',
        'charset':'utf8mb4',
        'cursorclass':pymysql.cursors.DictCursor
    }
    _connection=pymysql.connect(**config)
        
    def getAllUser(self):
        try:
            with self._connection.cursor() as cursor:
                sql='select * from `mo_digitalasset`'
                cursor.execute(sql)
                result=cursor.fetchall()
                return result
        except Exception as e:
            raise e

    
    def addDigitalAsset(self,digitalAsset):
        try:
            with self._connection.cursor() as cursor:
                sql="insert into `mo_digitalasset` (`id`,`Name`,`ContentType`,`CreateTime`,`CreateByUserId`,`Path`,`Size`) values(%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(digitalAsset.id,digitalAsset.name,digitalAsset.contentType,digitalAsset.createTime,digitalAsset.createByUserId,digitalAsset.path,digitalAsset.size))
                digitalAssetItemSql="insert into `mo_digitalasset_Item`(`id`,`name`,`contentType`,`description`,`digitalAssetId`,`createTime`,`createByUserId`) values(%s,%s,%s,%s,%s,%s,%s)"
                digitalAssetItemId=str(uuid.uuid4())
                cursor.execute(digitalAssetItemSql,(digitalAssetItemId,digitalAsset.name,digitalAsset.contentType,digitalAsset.name+"."+digitalAsset.contentType,digitalAsset.id,digitalAsset.createTime,digitalAsset.createByUserId))          
            self._connection.commit()
        except pymysql.OperationalError as e:
            if e.errno==2006:
                print("the connection have been closed")
                raise e           
            raise e      
        finally:
            cursor.close()
    def updateDigitalAsset(self,digitalAsset):
        try:
            with self._connection.cursor() as cursor:
                sql="update `mo_digitalasset` set `Name`=%s,`ContentType`=%s,`ModifyByUserId`=%s,`ModifyTime`=%s,`path`=%s,`Size`=%s where `Id`=%s"
                cursor.execute(sql,(digitalAsset.name,digitalAsset.contentType,digitalAsset.modifyByUserId,digitalAsset.modifyTime,digitalAsset.path,digitalAsset.size,digitalAsset.id))

            self._connection.commit()
        except Exception as ex:
            raise ex
    
    def getDigitalAssetById(self,id):
        try:
            with self._connection.cursor() as cursor:
                sql="select * from `mo_digitalasset` where `Id`=%s"
                cursor.execute(sql,(id))
                result=cursor.fetchone()
                print(result)
                return result
        except Exception as ex:
            raise ex

    def release(self):
        self._connection.close()
        
