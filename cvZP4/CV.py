diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
len_diameters = len(diameters)
num_good = 0
num = 0

for i in range(len_diameters):
    num += 1
   
    if abs(diameters[i] - 25.00) <= 0.05 and diameters[i] - 25.00 >= -0.05:
        
        print(f"\n {num}.{diameters[i]:6.2f}mm OK")
        num_good += 1
          
    else: 
        print(f"\n {num}.{diameters[i]:6.2f}mm BAD")
        
print("zmetku", num_good , "z" , len_diameters,"(",num_good * 10,"%",")")

    