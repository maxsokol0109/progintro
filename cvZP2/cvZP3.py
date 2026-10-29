# str = input("Enter the word: ")
# print("slovo =", str)

# strNum = len(str)
# print("Počet znaků:" , strNum)

# for i in range(strNum):
#     if(i == 0):
#         print("První znak:", str[i].capitalize())
    
#     elif(i == strNum-1):
#        print("Poslední znak:", str[i])

# velkými_písmeny = str.upper()
# print("Slovo velkými písmeny:", velkými_písmeny)

# reversed_word = str[::-1]
# print("Slovo obrácené:", reversed_word)

# if(reversed_word == str):
#     print(True)
# else:
#     print(False)


########################################## 
# for i in range(8 ,65, 8):
#     if i == 8:
#         print ("8 bitu:", 0 ,"az",2**i-1," // ",-(2**(i-1)),"az",2**(i-1)-1)
#     if i == 16:
#         print ("16 bitu:", 0 ,"az",2**i-1," // ",-(2**(i-1)),"az",2**(i-1)-1)
#     if i == 32:
#         print ("32 bitu:", 0 ,"az",2**i-1," // ",-(2**(i-1)),"az",2**(i-1)-1)
#     if i == 64:
#         print ("64 bitu:", 0 ,"az",2**i-1," // ",-(2**(i-1)),"az",2**(i-1)-1)

#########################################


# KladneCislo = int(input("Zadej kladné číslo: "))
# x = KladneCislo
# leftovers_list = []
# count = 0


# while KladneCislo > 0:
#       x = KladneCislo % 2
#       KladneCis21lo = KladneCislo // 2
#       leftovers_list.append(x)

# leftovers_list.reverse()
# print("Binární číslo:", leftovers_list)

# print("kontrola:",bin(x))

# print("pocet_bitu", len(leftovers_list))

# for i in range(len(leftovers_list)):
#       if leftovers_list[i] == 1:
#             count = count + 1

# print("Počet jedniček:", count)

#######################################################

# binarni_list = []
# binarni_int_list = []
# decimalni_cislo = 0

# binarni_cislo = str(input("Zadej binární číslo: "))

# for i in range(len(binarni_cislo)):
#       if binarni_cislo[i] == "1":
#             binarni_int_list.append(1)
#       elif binarni_cislo[i] == "0":
#             binarni_int_list.append(0)
# binarni_int_list.reverse() 

# for i in range(len(binarni_int_list)):
#       if binarni_int_list[i] == 1:
#             decimalni_cislo = decimalni_cislo + 2**(i)

# print("Decimalní číslo:", decimalni_cislo)

############################################################

# slovo =str(input("napiste slovo: "))
# str_list = []


# for i in range(len(slovo)):
#     code = ord(slovo[i])
#     print(slovo[i],"",f"{code:04X}"," B ",len(slovo[i].encode("utf-8")))
   
# print("bity: ",len(slovo.encode("utf-8")))
# print("znacky", len(slovo))

###########################################################

# שלב 1: קליטת הנתונים והכנתם
slovo = input("Napiš větu: ")
slovo = slovo.lower() # הפיכת כל האותיות לקטנות
strNum = len(slovo)
letters_count = {} # יצירת המילון הריק

# שלב 2: ספירת האותיות לתוך המילון
for i in range(strNum):
    # סינון: רק אם התו הוא אות חוקית (מתעלם מרווחים וסימני פיסוק)
    if slovo[i].isalpha():
        # בדיקה האם האות כבר קיימת במילון
        if slovo[i] in letters_count:
            letters_count[slovo[i]] = letters_count[slovo[i]] + 1 # הגדלת המונה
        else:
            letters_count[slovo[i]] = 1 # הוספת האות בפעם הראשונה

# שלב 3: מיון המילון והדפסת התדירויות
# הפיכת המילון לרשימת צמדים ומיון בעזרת שופט (למבדא)
sorted_letters = sorted(letters_count.items(), key=lambda x: (-x[1], x[0]))

print("\nČetnosti písmen:")
# מעבר על הרשימה הממוינת והדפסת כל צמד בצורה יפה
for letter, count in sorted_letters:
    print(letter, "-", count)

# שלב 4: הדפסת מספר האותיות השונות (אורך המילון)
print("\nPočet různých písmen:", len(letters_count))



    
