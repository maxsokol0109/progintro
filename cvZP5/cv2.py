

def convert_temperature(value, from_unit, to_unit):
    if(from_unit == "F" and to_unit == "C"):
        to_unit = (value - 32) * 5/9
        return round(to_unit, 2)

    elif (from_unit == "C" and to_unit == "F"):
        to_unit = value * 9/5 + 32
        return round(to_unit, 2)


 
    elif (from_unit == "K" and to_unit == "F"):
        to_unit = 5/9 * (value - 32) + 273.15
        return round(to_unit, 2)

    elif (from_unit == "F" and to_unit == "K"):
        to_unit = (value + 459.67) * (5/9)
        return to_unit

    

    elif (from_unit == "K" and to_unit == "C"):
        to_unit = round(value - 273.15) 
        return to_unit
    
    elif (from_unit == "C" and to_unit == "K"):
        to_unit = value + 273.15
        return to_unit


print(convert_temperature(40, "C", "F"))   # 212.0
print(convert_temperature(0, "K", "C"))     # -273.15
print(convert_temperature(-40, "C", "F"))   # -40.0
print(convert_temperature(20, "C", "X"))    # None


print(f"{'C':<10} | {'F':<10} | {'K':<10}")

for i in range(-40,101, 20):
    c = i
    f = convert_temperature(i,"C", "F")
    k = convert_temperature(i,"C", "K")

    print(f"{c:<10} | {f:<10} | {k:<10}")
   
