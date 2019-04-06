import time
# time.sleep(secs)을 사용하기 위한 모듈, 주어진 초만큼 프로세스를 정지시킵니다.
from influxdb import InfluxDBClient
# InfluxDBClient(host, port, id, password, database)를 사용하기 위한 모듈입니다.
from random import uniform
# uniform(a,b)을 사용하기 위한 모듈, a~b 사이의 float형 난수 생성합니다.
 
dbClient = InfluxDBClient('localhost', 8086, 'root', 'root', 'mydb2')
# dbClient에 InfluxDBClient를 사용하여 DB의 정보를 삽입합니다.
 
def write():
    loginEvents = [{"measurement": "UserLogins", "fields": {"SessionDuration": uniform(1.0, 200.0)}}]
    dbClient.write_points(loginEvents)
    time.sleep(0.001)
# write() 함수를 생성합니다.
# write() 함수는 loginEvents에 1.0 와 200.0 사이의 난수를 가지는 'SessionDuration'을 입력한 후, 연결된 DB에 삽입하고, 0.001초 정지합니다.
  
while True:
    write()
# write()를 무한으로 반복합니다.