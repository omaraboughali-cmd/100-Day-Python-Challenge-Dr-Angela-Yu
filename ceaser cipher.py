import string
lowercase_list = list(string.ascii_lowercase)
def ceaser():
    
    direction = input("encrypt or decrypt ?")
    original_text = input("type in the text you want to cipher")
    shift = int(input("how many letters to shift"))

    if direction == "decode":
        shift *= -1
    ceasered_text = ""
    for i in original_text:
        if i not in lowercase_list:
            ceasered_text += str(i)
        for j in lowercase_list:
            if i == j:
                ceasered_text += lowercase_list[(lowercase_list.index(j)+shift)%len(lowercase_list)] 
    print(ceasered_text)  
should_continue = input("continue?")
while True:
    ceaser()
    should_continue = input("continue?")
    if should_continue == "no":
        break