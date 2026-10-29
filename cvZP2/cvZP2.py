seconds = float(input("Enter the number of seconds: ")) 
x = seconds

days = int(seconds) // 86400
x = x % 86400

hours = x // 3600
x = x % 3600

minutes = x // 60
x = x % 60

seconds = x

print( days,"d   ", hours, ": ", minutes, ": ", seconds, ":")