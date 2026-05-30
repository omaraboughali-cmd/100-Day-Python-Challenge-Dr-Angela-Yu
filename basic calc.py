def multiply(a , b):
    return a * b


def divide(a , b):
    return a / b


def subtract(a , b):
    return a - b


def add(a , b):
    return a + b            
big_num = 0
def calc():

    first_num = int(input("what is the first num "))
    operation = input("choose operator + - * / ")    
    second_num = int(input("enter second num "))



    operations = {"+":add , "-":subtract , "*":multiply , "/":divide}

    num = int(operations[operation](first_num,second_num))
    print(f"{first_num} {operation} {second_num} = {num}")
    print(num)
    big_num = num
    
    while True:
        again = input("if you want to do another calculation type in y ")
        
        if again == "y":
            new_num = int(input("enter number "))
            new_operation = input("enter operation ")
            neo_num = int(operations[new_operation](big_num,new_num))
            print(f"{big_num} {new_operation} {new_num} = {neo_num}")
            print(neo_num)
            big_num = neo_num

        elif again == "start over":
            calc()
        else:
            break        
     
calc()
  
