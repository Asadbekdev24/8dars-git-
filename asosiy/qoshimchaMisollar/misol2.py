import os
os.system("cls")

son1=int(input("A = "))
son2=int(input("B = "))

listSon=[son1]
soni=0
while(son1/2>son2):
    son1/=2
    listSon.append(son1)
    soni+=1

print(soni)
for el in listSon:
    print(el,"->", end="")
