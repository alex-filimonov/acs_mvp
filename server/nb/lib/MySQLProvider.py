

import pymysql

class MySQLProvider():
    def __init__(self):
        self.connect=None

    def connected(self,host,port,database,user,password):
        self.connect = pymysql.connect(host=host,user=user,password=password,db=database,port=int(port))

    def getAllCPE(self):
        sql = "Select id,serial_number,vendor_name,model_name,all_inform,first_inform,last_inform from cpe "
        cursor = self.connect.cursor()
        cursor.execute(sql)
        ret=[]
        rows = cursor.fetchall()
        for row in rows:
            ret.append({'id':row[0],'serial_number':row[1],'vendor_name':row[2],'model_name':row[3],'all_inform':row[4],'first_inform':row[5],'last_inform':row[6]})
        return ret


    def getCPEbyID(self,id):
        sql = "Select id,serial_number,vendor_name,model_name,all_inform,first_inform,last_inform from cpe Where id = %s "
        cursor = self.connect.cursor()
        cursor.execute(sql, ( id ) )
        row=cursor.fetchone()
        if row==None:
            return None
        ret={'id':row[0],'serial_number':row[1],'vendor_name':row[2],'model_name':row[3],'all_inform':row[4],'first_inform':row[5],'last_inform':row[6]}
        return ret 

    def getCommandsByCpeID(self,id):
        sql = """
                Select c.id, c.request, c.response, c.status_id, c.create_time, c.update_time,t.command_name
                from commands c
                    left join commands_type t on (c.command=t.id)
                where c.cpe_id=%s 
                order by c.id desc
                """
        cursor = self.connect.cursor()
        cursor.execute(sql,(id))
        ret=[]
        rows = cursor.fetchall()
        for row in rows:
            ret.append({'id':row[0],'request':row[1],'response':row[2],'status_id':row[3],'create_time':row[4],'update_time':row[5],'command_name':row[6]})
        return ret

    def insertCPECommand(self,cpe_id,command_type,input_parametr):
        sql = "insert into commands (cpe_id,command,request,status_id,create_time) values (%s,%s,%s,%s,%s)"
#        sql = "insert into commands (cpe_id) values (%s)"
        cursor = self.connect.cursor()
        cursor.execute(sql, (str(cpe_id),str(command_type),input_parametr,str(0),None ))
        self.connect.commit() 

    def deleteCPECommands(self,id):
        sql = "delete from  commands where id=%s"
        cursor = self.connect.cursor()
        cursor.execute(sql, (str(id)))
        self.connect.commit() 

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

    def getCommandTypeList(self):
        sql = "Select id,command_name from commands_type "
        cursor = self.connect.cursor()
        cursor.execute(sql)
        ret=[]
        rows = cursor.fetchall()
        for row in rows:
            ret.append({'id':row[0],'command_name':row[1]})
        return ret


    




    

