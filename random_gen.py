import random
file=open("output.txt","r")
target=open("test file","w")
lines=file.readlines()
x=0
for i in range(0,99):
    x=random.randint(1,2350)
    x=2*x+1
    target.write(lines[x+1]+"\n")
    target.write(lines[x+2]+"\n")
    target.write("telic role:"+"\n")
    
    
