import pymysql

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
    connection=pymysql.connect(**config)
    def getAllUser(self):
        try:
            with self.connection.cursor() as cursor:
                sql='select * from `mo_digitalasset`'
                cursor.execute(sql)
                result=cursor.fetchall()
                for item in result:
                    print(item)
                return result
        except Exception as e:
            raise e

    
    def addDigitalAsset(self,digitalAsset):
        try:
            with self.connection.cursor() as cursor:
                sql="insert into `mo_digitalasset` (`id`,`Name`,`ContentType`,`CreateTime`,`CreateByUserId`,`Path`,`Size`) values(%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(digitalAsset.id,digitalAsset.name,digitalAsset.contentType,digitalAsset.createTime,digitalAsset.createByUserId,digitalAsset.path,digitalAsset.size))
                
            self.connection.commit()
        except Exception as e:
            raise e

    def updateDigitalAsset(self,digitalAsset):
        try:
            with self.connection.cursor() as cursor:
                sql="update `mo_digitalasset` set `Name`=%s,`ContentType`=%s,`ModifyByUserId`=%s,`ModifyTime`=%s,`path`=%s,`Size`=%s where `Id`=%s"
                cursor.execute(sql,(digitalAsset.name,digitalAsset.contentType,digitalAsset.modifyByUserId,digitalAsset.modifyTime,digitalAsset.path,digitalAsset.size,digitalAsset.id))

            self.connection.commit()
        except Exception as ex:
            raise ex
    
    def getDigitalAssetById(self,id):
        try:
            with self.connection.cursor() as cursor:
                sql="select * from `mo_digitalasset` where `Id`=%s"
                cursor.execute(sql,(id))
                result=cursor.fetchone()
                return result
        except Exception as ex:
            raise ex

    def release(self):
        self.connection.close()
        
