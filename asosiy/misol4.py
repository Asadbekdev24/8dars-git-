import os
os.system("cls")

matn=input("Matn kiriting : ")

chapBelgilar="1QAZ2WSX3EDG45RTFGVB"
ongBelgilar="67YUHJNM8IK,9OL.0P;/'"

chapCount=0
ongCount=0

for el in matn:
    if el.capitalize() in chapBelgilar:
        chapCount+=1
    if el.capitalize() in ongBelgilar:
        ongCount+=1

print("Chap qo'l bilan yozilgan harflar soni = ", chapCount)
print("O'ng qo'l bilan yozilgan harflar soni = ", ongCount)
