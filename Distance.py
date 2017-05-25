from math import sin, cos, sqrt, atan2, radians

def calculateDistance(lat1,lon1,lat2,lon2):
    # approximate radius of earth in km
    R = 6373.393

    lat_1 = radians(lat1)
    lon_1 = radians(lon1)
    lat_2 = radians(lat2)
    lon_2 = radians(lon2)

    dlon = lon_2 - lon_1
    dlat = lat_2 - lat_1

    a = sin(dlat / 2)**2 + cos(lat_1) * cos(lat_2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


#print calculateDistance(34.49199,-114.755,42.98915,-71.3436)
year=2000
for k in range(17):
    readingfilename = "Year_County_Data_Nodes/Part_" + str(year) + ".csv"
    writingfilename = "Year_County_Data_Edges/Part_" + str(year) + "_Network.csv"
    fo=open(readingfilename,"r+")
    go=open(writingfilename,"w+")
    year=year+1
    go.write("Source,Target,Type,Id,Weight,Sourcename,Targetname" + "\n")
    records=fo.readlines()
    edgecount=0
    for i in range(1,len(records)):
        for j in range(1,len(records)):
            if(i!=j):
                #print records[i]
                distance = calculateDistance(float(records[i].split(",")[8]),float(records[i].split(",")[9]),float(records[j].split(",")[8]),float(records[j].split(",")[9]))
                if(distance<1000):
                    go.write(str(i-1) + "," + str(j-1) + "," + "Undirected" + "," + str(edgecount) + "," + str(distance) + "," + records[i].split(",")[2] + "," + records[j].split(",")[2] + "\n")
                    edgecount=edgecount+1
