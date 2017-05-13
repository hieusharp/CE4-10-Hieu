
##Welcome t’o our shop, what do you want (C, R, U, D)? C
##Enter new ===item: Jeans
##Our items: T-Shirt, Sweater, Jeans
##
##Welcome to our shop, what do you want (C, R, U, D)? R
##Our items: T-Shirt, Sweater, Jeans
##
##Welcome to our shop, what do you want (C, R, U, D)? U
##Update position? 1
##New item? Skirt
##Our items:  T-Shirt, Skirt, Jeans
##
##Welcome to our shop, what do you want (C, R, U, D)? D
##Delete position? 2
##Our items:  T-Shirt, Skirt, Jeans


clothes = ["T-Shirt", "Sweat" ]


print("==========================================")
print("Create = C, Reveal = R, Update = U, Delete = D")
print("==========================================")
print("Welcome to our shop.")
while True:
    action = input("What do you want (C, R, U, D) ?")
    print(action)
    action = action.upper()

##    print ("Clothes in shop: ")
##    item_no = 1
##    for clothe in clothes:
##        print("{0}. {1}".format(item_no, clothe))
    
    if action == "C":
        new_item = input("Enter new item: ")
        clothes.append(new_item)
        print("Our items now:", ", ".join(clothes))
    elif action == "R":
        print("Our items now:", ", ".join(clothes))
        
    elif action == "U":
        item_no = int(input("Update new position: "))
        item_new = input("New item: ")
        clothes.insert(item_no, item_new)
        print("Our items now:", ", ".join(clothes))

    elif action == "D":
        item_no = int(input("Delete position: "))
        clothes.pop(item_no-1)
        print("Our items now:", ", ".join(clothes))
    else:
        print("I dont get it.")
        
 
