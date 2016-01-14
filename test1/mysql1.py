#coding=utf-8
import mysql.connector

#二进制转换成string
def convert(data):
        print('调用转换函数')
        #print(data)
        return str(data,bytearray)



conn= mysql.connector.connect(
        host='192.168.110.27',
        port = 3306,
        user='root',
        passwd='passwd',
        db ='Cloud',
        )
cur = conn.cursor()

cur.execute("select DevHistory_201512.* from DevHistory_201512,Devices where (DevHistory_201512.DevId = Devices.DevId ) and Devices.DevTypeId = 481 and DevHistory_201512.DataDate = 21;");

sqlValue = cur.fetchall()
sqlLength = len(sqlValue)
print sqlLength
print sqlValue

data = sqlValue[0][03]

insertdata = convert(data)
print(insertdata)

#插入数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")





    
    
    
    


#获取值的cur游标关闭
cur.close()
#事务提交
conn.commit()
#连接关闭
conn.close()
    

    