
num_year = 0

for year in range(1890,2031):

        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
          num_year += 1
          print(f"{year}", end="\t")
        
        if (num_year % 10 == 0):
          print()
          
print ('-'* 50)
print(f"num roku je {num_year}")

 