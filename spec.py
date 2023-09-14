from gdx import gdx
gdx = gdx.gdx()
 
#initializes connection 
gdx.open(connection='usb')

#selects the one and only sensor on the spectrometer
gdx.select_sensors([1])

#starts collecting data
time_period = 100 #samples at every 100 milliseconds, sampling less than 10 may be problematic
gdx.start(time_period) 

#loop needs to be fast enough to keep up with the time period 
#the range basically specifies how long we want to collect data, kind of janky
for i in range(0,5):
    measurements = gdx.read()
    if measurements == None: 
        break 
    print(measurements) #need to return measurements and send to base
 
gdx.stop()
gdx.close()