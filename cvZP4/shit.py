def welcome_participant():
    name = input("enter your first name : ")
    surname = input("enter your surname: ")

    full_name = name + " " + surname

    print("welcome to the event, " + full_name + "!")
welcome_participant() #call it

def check_age(age):
    if age < 18:
        print("go fuck yourself")
    if age >= 18:
        print("good")
participant_age = int(input("enter age: "))
check_age(participant_age)

def calculator_price(has_isic,full_price):
    if has_isic:
        final_price = full_price * 0.7
    else:
        final_price = full_price
    return final_price
full_price = 1800
answer = input("do you have isic : ")
has_isic = answer.lower() == "yes"
price = calculator_price(has_isic,full_price)
print("your praice is ", price, "czk")