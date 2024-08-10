import os
os.system("cls")
from json import dumps

son=int(input("Son kiriting : "))

raqam=[0,1,2,3,4,5,6,7,8,9]

nechta=[]
qaysiRaqam=[]

javob={}

for el in raqam:
    if str(son).count(str(el))>=1:
        nechta.append(str(son).count(str(el)))
        qaysiRaqam.append(el)

javob=dict(zip(qaysiRaqam,nechta))
print(dumps(javob, indent=4))
