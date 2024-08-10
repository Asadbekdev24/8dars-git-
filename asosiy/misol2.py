import os
os.system("cls")

def chiqar(son:int, royhat:list):
    yangi_list=sorted(royhat, key=lambda qiymat:qiymat["narxi"], reverse=True)
    for i in range(son):
        print(yangi_list[i])

list1=[
    {"nomi":"Olma", "narxi":13000},
    {"nomi":"Olcha", "narxi":12000},
    {"nomi":"Anor", "narxi":11000},
    {"nomi":"Uzum", "narxi":17000},
    {"nomi":"Anor", "narxi":45000},
]


son=int(input("Nechta narxi qimmat mahsulotni chiqarmoqchisiz? "))

(chiqar(son,list1))
