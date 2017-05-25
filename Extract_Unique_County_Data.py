records=[]
fo=open("Network.csv","r+")
records = fo.readlines()
result=[]
for i in range(len(records)):
    temp=records[i].split(",")
    tempstring = temp[0] + "," + temp[1] + "," + temp[2]
    if(tempstring not in result):
        result.append(tempstring)
go=open("data.csv","w+")
for j in range(len(result)):
    go.write(result[j] + "\n")
print len(result)
print len(records)