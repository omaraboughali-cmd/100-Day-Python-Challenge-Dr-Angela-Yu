height = int(input("enter your height"))
age = int(input("enter your age"))
total = 0
want_photo = input("would you like a photo")
if height > 120:
    if age  < 12:
        print("pay $5")
        total += 5
    elif  18 > age > 12:
        print("pay $7")
        total += 7
    elif age >= 18:
        if 55 >= age >= 45:
            print("free ride")
        else:
            print("pay $12")
            total += 12
if want_photo == "yes":
    print("extra $3")
    total += 3            
print("please pay $"+str(total))
