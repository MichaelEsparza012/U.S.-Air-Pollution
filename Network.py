records=[]
with open("Resultant.csv","r") as f:
 for line in f:
    records.append(line)
year=2000
for i in range(17):
    filname="Part_" + str(year) + ".csv"
    fo=open("Year_County_Data_Nodes/" +filname,"a+")
    fo.write("State,City,Label,Year,SO,NO,CO,O3,Latitude,Longitude" + "\n")
    fo.close()
    year=year+1

for i in range(1,len(records)):
    temp = records[i].split(",")
    filname = "Part_" + temp[3] + ".csv"
    fo = open("Year_County_Data_Nodes/" +filname,"a+")
    fo.write(records[i])
    fo.close()





