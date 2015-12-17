import mysql.connector
config={'host':'192.168.110.27',
        'user':'root',
        'password':'password@2014',
        'port':3306 ,
        'database':'pytest',
        'charset':'utf8'
        }
try:
  cnn=mysql.connector.connect(**config)
except mysql.connector.Error as e:
  print('connect fails!{}'.format(e))