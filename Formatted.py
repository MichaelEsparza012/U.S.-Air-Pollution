fo=open("Network.csv","r+")
go=open("locations.csv","r+")
ho=open("Resultant.csv","w+")

frecords=fo.readlines()
grecords=go.readlines()
ho.write("State,City,County,Year,SO,NO,CO,O3,Latitude,Longitude" + "\n")
for i in range(1,len(frecords)):
    for j in range(1,len(grecords)):
        temp=frecords[i].split(",")
        fstring = temp[0] + "," + temp[1] + "," + temp[2]
        temp=grecords[j].split(",")
        gstring= temp[0] + "," + temp[1] + "," + temp[2]
        if(fstring==gstring):
            state=frecords[i].split(",")[0]
            city=frecords[i].split(",")[1]
            county=frecords[i].split(",")[2]
            year=frecords[i].split(",")[3]
            so=frecords[i].split(",")[4]
            no=frecords[i].split(",")[5]
            co=frecords[i].split(",")[6]
            oo=frecords[i].split(",")[7].strip()
            lat=grecords[j].split(",")[3]
            lon=grecords[j].split(",")[4]
            ho.write(state + "," + city + "," + county + ","  + year + "," + so + "," + no + "," + co + "," + oo + "," + lat + ","+ lon)
