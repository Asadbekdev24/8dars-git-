import os
os.system("cls")

soz=input("Soz kiriting : ")

for i in range(0,len(soz)):
    for j in range(0,i+1):
        print(soz[j], end="")
    print()
for k in range(len(soz)-2,-1,-1):
    for j in range(0,k+1):
        print(soz[j], end="")
    print()