#coding=utf-8
import mysql.connector

conn= mysql.connector.connect(
        host='t.10000bee.com',
        port = 3306,
        user='root',
        passwd='pass9cuo@2014',
        db ='Cloud',
        )
cur = conn.cursor()

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

cur.execute("select DevHistory_201512.* from DevHistory_201512,Devices where (DevHistory_201512.DevId = Devices.DevId ) and Devices.DevTypeId = 481 and DevHistory_201512.DataDate = 21;");

# w1=cur.execute("select * from Users where UserId = '17825800';");
# print w1;
ww = cur.fetchall();
print len(ww)
print ww

cur.close()
conn.commit()
conn.close()

#二进制转换成string
#def convert ():
    
    
    
    
    
    
    

    