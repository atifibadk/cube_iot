import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
import time 
import MySQLdb

conn = MySQLdb.connect("data.cojvodnw3hk2.ap-south-1.rds.amazonaws.com","user","ibadkhan","cube_iot") 
c = conn.cursor()

while True:
    sensor = BMP085.BMP085()
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    temp=temperature
    humi=humidity
    pree=sensor.read_sealevel_pressure()
    print "Values from sensor"
    print ("Humidity = {} %; Temperature = {} C".format(humi, temp))
    print 'Pressure = {0:0.2f} Pa'.format(pree)
    
    c.execute("UPDATE value1 set temp=%s,humidity=%s,pressure=%s where pkey=1",(temp,humi,pree))
    conn.commit()

    c.execute("select * from value1")
    rows=c.fetchall()
    for i in rows:
	print i
    



    time.sleep(3)
    
