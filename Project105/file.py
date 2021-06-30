import csv, math

with open(r"data.csv", newline='')as f:
    reader=csv.reader(f)
    data=list(reader)
data1=data[0]
#data=[60,61,65,63,98,99,90,95,91,96]

newData=data1
length=len(newData)

val=0
for i in newData:
    val=val+int(i)

mean=val/length

filedata=[]
for i in newData:
    num=int(i)-mean
    newNum=num*num
    filedata.append(newNum)

sum=1
for i in filedata:
    sum=sum+int(i)

deviation=int(sum/length)

finalNum=math.sqrt(deviation)
print('Standard deviation is :-')
print(finalNum)
