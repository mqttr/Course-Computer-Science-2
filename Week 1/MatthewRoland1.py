# Main Menu Display
def main_menu():
    # Display main menu
    print(r"----MAIN MENU----")
    print(r"s: Shop")
    print(r"x: Exit")
        
    userCommand = input("Option: ").strip().lower()
    while True:
        
        # Invalid Response Handling
        if userCommand == "s":
            return "s" # Shop 
        elif userCommand == "x":
            return "x" # Exit 
        else:
            userCommand = input("Invalid (s/x): ").strip().lower()
            
def cart_menu():
    item = ""
    
    # Display Shopping Cart Menu
    print(r"----CART MENU----")
    
    print(f"1: Cookie - $1.50")
    print(f"2: Sandwich - $4.00") 
    print(f"3: Water - $1.00") 

    
    # counter = 1

    # for ele in storePrices.keys():
    #     print(f"{counter}: {ele.title()} - ${storePrices[ele]:0.2f}")
        
    #     counter+=1

    userCommand = input("Item: ").strip()
    
    #  Invalid Response Handling (Repeat until correct response)
    while True:
        if userCommand == "1" or userCommand == "2" or userCommand == "3": 
            break
        userCommand = input(f"Invalid (1-3): ").strip()
    
    return int(userCommand) 

def main():
    storePrices = {"cookie":1.50, "sandwich":4.00, "water":1.00}
    userCart = {"cookie":0, "sandwich":0, "water":0}

    # TODO Tracks item count & total cost of all items
    gameState = True
    while gameState:
        userCommand = main_menu()
        if userCommand == "x":
            break
        else:
            item = cart_menu()
            if item == 1:
                word = "cookie"
            elif item == 2:
                word = "sandwich"
            else:
                word = "water"

            userCart[word]+=1
            
            print(f"Added {word}")

    # Print End Scheme
    print(r"-------------------")
    
    grandTotal = 0.00
    for ele in userCart.keys():
        print(f"({userCart[ele]}) {ele.title()} = ${userCart[ele] * storePrices[ele]:0.2f}")
        grandTotal+=userCart[ele] * storePrices[ele]

    print("-------------------")
    print(f"GRAND TOTAL = ${grandTotal:0.2f}")
    print("-------------------")
    gameState = False
    exit()
    

if __name__ == "__main__":
    main()