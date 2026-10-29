
#RRMMDD/XXXX
def normalize(birth_number):
    # 1. בדיקה שהקלט הוא מחרוזת
    if str(birth_number).count("/") == 0:
        return None

    # 2. הסרת לוכסן ורווחים
    clean = birth_number.replace("/", "").replace(" ", "")

    # 3. בדיקה שהתוצאה מכילה בדיוק 10 ספרות
    if len(clean) == 10 and clean.isdigit():
        return clean
    else:
        return None

print(normalize("540101/1234"))



def is_valid(birth_number):
   
   check = normalize(birth_number)

   if(int(check) % 11 == 0):
       return True
   else:
       return False
print(is_valid("736028/5163"))



def gender(birth_number):
    check = normalize(birth_number)

    # חילוץ ספרות החודש (תווים באינדקס 2 ו-3)
    month = int(check[2:4])  # string[start:stop]  <x:x)

    if month > 50:
        return "zena"
    else:
        return "muz"



# RRMMDD/XXXX
def birth_date(birth_number):

    clean = normalize(birth_number)
    if clean == None:
        return None
    
    gender_check = gender(birth_number)

    year = int(clean[0:2])
    month = int(clean[2:4])
    day = int(clean[4:6])

    if year <= 53:
        year += 2000

    elif year >=54:
        year += 1900
        

    if(gender_check == "muz"):
        return f"muz {str(day).zfill(2)}.{str(month).zfill(2)}.{year}"
    
    elif gender_check == "zena":
        month -=50
        return f"zena {str(day).zfill(2)}.{str(month).zfill(2)}.{year}"
    
print(birth_date("/5163"))     
print(birth_date("990101/1230"))    
    
