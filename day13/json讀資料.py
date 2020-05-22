import json
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
ChineseFont2=FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc')
import numpy as np
from math import cos

with open('day13/tt.json',encoding='UTF-8')as json_file:
    data=json.loads(json_file.read())
    json_file.close()

def setcolor(aqi):
    tenwei,gerwei=0,0
    tenwei=int(aqi/16)
    gerwei=int(aqi%16)
    jinweinum = ""
    if tenwei >=10:
        jinweinum=chr(tenwei+55)
    else:
        jinweinum=str(tenwei)
    if gerwei >=10:
        jinweinum+=chr(tenwei+55)
    else:
        jinweinum+=str(tenwei)

    color="#"
    color+=jinweinum
    color+="0000"
    return color

index=0
site_list=[]
lon_list=[]
lat_list=[]
aqi_list=[]
while index < len(data):
    site_list.append(data[index]["SiteName"])
    lon_list.append(float(data[index]["Longitude"]))
    lat_list.append(float(data[index]["Latitude"]))
    aqi_list.append(float(data[index]["AQI"]))
    index+=1

#fig = plt.figure()
#ax=fig.add_subplot(111)
plt.xlim(118,122)
plt.ylim(20,27)
x=list(0 for x in range(len(site_list)))
y=list(0 for x in range(len(site_list)))
color=list(0 for x in range(len(site_list)))
for i in range(len(site_list)):
    #x[i]=float(lon_list[i])*111.320*cos(float(lat_list[i])/180*3.14159262)/100
    #y[i]=float(lat_list[i])*110.574/100
    #plt.text(x[i],y[i],site_list[i],FontProperties=ChineseFont2)
    print(lat_list[i],lon_list[i],site_list[i],aqi_list[i])
    #ax.axis(120,124,21,28)
    x[i]=float(lon_list[i])
    y[i]=float(lat_list[i])
    color[i]=setcolor(aqi_list[i])
    print(color[i])

plt.scatter(x=x,y=y,color=color)
plt.ylabel("y_label")
plt.xlabel("x_label")
plt.title("Title")

plt.show()