

import pymysql

class MySQLProvider():
    def __init__(self):
        self.connect=None

    def connected(self,host,port,database,user,password):
        self.connect = pymysql.connect(host=host,user=user,password=password,db=database,port=int(port))



    def getCPEbySN(self,serial_number):
        sql = "Select id,serial_number,vendor_name,model_name,all_inform,first_inform,last_inform from cpe Where serial_number = %s "
        cursor = self.connect.cursor()
        cursor.execute(sql, ( serial_number ) )
        row=cursor.fetchone()
        if row==None:
            return None
        ret={'id':row[0],'serial_number':row[1],'vendor_name':row[2],'model_name':row[3],'all_inform':row[4],'first_inform':row[5],'last_inform':row[6]}
        return ret 

    def insertCPE(self,serial_number,vendor_name,model_name,all_inform):
        sql = "insert into cpe (serial_number,vendor_name,model_name,all_inform,first_inform,last_inform) values (%s,%s,%s,%s,%s,%s)"
        cursor = self.connect.cursor()
        cursor.execute(sql, (serial_number,vendor_name,model_name,all_inform,None,None ) )
        self.connect.commit() 

    def updateCPE(self,id,vendor_name,model_name,all_inform):
        sql = "update cpe set vendor_name=%s,model_name=%s,last_inform=%s,all_inform=%s where id=%s"
        cursor = self.connect.cursor()
        cursor.execute(sql, (vendor_name,model_name,None,all_inform,id ) )
        self.connect.commit() 





