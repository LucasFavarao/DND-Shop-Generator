import csv
import random
from django.core.management.base import BaseCommand

F_DEFAULT_ITEMS="itemList.csv"

def printItems(rows):
    for row in rows:
        print("*********************************************************")
        print('Item Name: ',row["item_name"])
        print('Item Price:',row["price"])
        print('Item Weight: ',row["item_weight"])
        print('Shop Vendor:',row["shop_vendor"])
        print('Rarity:',row["rarity"])
    print("*********************************************************")


def randomSelection(totalItems,n,shopType):
    shopItems = [{} for _ in range(n)]
    i = 0
    k=0
    while (k!=n):
        chance=0
        roll = random.randrange(1,100)
        if (totalItems[i]['shop_vendor'].lower()==shopType):
            chance+=80
        if (totalItems[i]['rarity'].lower()=='common'):
            chance+=10
        elif (totalItems[i]['rarity'].lower()=='uncommon'):
            chance+=5
        elif(totalItems[i]['rarity'].lower()=='rare'):
            chance+=5
        if (roll<chance):
            shopItems[k]= totalItems[i].copy()
            k+=1
        i+=1
        if (i==len(totalItems)):
            i=0
        
    return shopItems

def fileHandeling ():
    rows = []
    with open(F_DEFAULT_ITEMS,mode='r',encoding='utf-8') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            row['price']=convertMoneyType(row['price'])
            rows.append(row)
        return rows


def convertMoneyType(row):
    sum = 0.0
    if "gp" in row.lower():
        price_digits = ''.join(filter(str.isdigit, row))
        numPieces=int(price_digits) if price_digits else 0
        sum+=numPieces
    
    elif "sp" in row.lower():
        price_digits=''.join(filter(str.isdigit,row))
        numPieces=int(price_digits) if price_digits else 0
        sum+=(numPieces*0.1)   
    
    elif "cp" in row.lower():
        price_digits=''.join(filter(str.isdigit,row))
        numPieces=int(price_digits) if price_digits else 0
        sum+=numPieces*0.01

    return sum

row=fileHandeling()
printItems(row)
