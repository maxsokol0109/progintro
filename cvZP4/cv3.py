def IFprvocislo(n):
    n = int(input("add num: ")) # 20
    limit = int(n**0.5)

    for i in range(2,limit+1):
        if(n % i == 0):
           return False
    else:
        return True
    
#print(IFprvocislo(40))
 
##############################################

pocet = 0 

for num in range(2,101):

    for i in range(2,num):
        if (num % i == 0):
            break

    else:
        print(num , end= " ")
        pocet += 1

###################################
print()

d = 2
num = int(input("add num: "))

while num > 1:
    if (num % d == 0):
        
        if (num == d):
            print(d)  # הגורם האחרון - מדפיסים בלי כוכבית בסוף
        else:
            print(d, end=" * ")  # יש עוד גורמים בהמשך
        
        num = num // d
    else:
        d += 1



        


        

