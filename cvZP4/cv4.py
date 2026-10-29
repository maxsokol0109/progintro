
num = int(input("napis num: "))
while(num % 2 == 0 and num > 0):
     num = int(input("napis lichi a kladne cislo: "))


start = 0

stars = 1
space = num // 2
    
for i in range(start,num):
    if(i < num//2):
           
         print("-" *(space) + (stars * "*") + "-" *(space))
         stars += 2
         space -=1
    
    elif(stars == num):
        print("*" * num)
        stars-=2
        space+=1
        
         
    if(i > num // 2):
        print("-" *(space) + (stars * "*") + "-" *(space))
        stars-=2
        space+=1
        
         
         
    

         
    

    

     
     
     
     








