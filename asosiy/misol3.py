import os
os.system("cls")


son=input("Son kiriting : ")

soni=0
for el in son:
    if int(el)==0:
        soni+=1
    else:
        break
print(soni)
