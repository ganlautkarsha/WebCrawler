from distutils.command.check import check
file=open("input","r")
array=[[]]
length=0
for line in file:
    length=len(line)
    array.append(list(line.strip("\n")))

print (array)
checkup=True
checkdown=True
checkright=True
checkleft=True
sum_=0
change=False
del array[0]
print(array)

for i in range(10):
    for i in range(0,length):
        for j in range(0,length):

            if i==0:
                checkup=False
            if j==0:
                checkleft=False
            if j==length-1:
                checkright=False
            if i==length-1:
                checkdown=False
            
            if checkup:
                if int(array[i-1][j]==1):
                    sum_+=1
                
            if checkright:
                if int(array[i][j+1]==1):
                    sum_+=1
                
            if checkdown:
                if int(array[i+1][j]==1):
                    sum_+=1
                
            if checkleft:
                if int(array[i][j-1]==1):
                    sum_+=1
                
            if sum_ >= 2:
                array[i][j]=1
            checkup=True
            checkdown=True
            checkright=True
            checkleft=True
                
    
print(array)


