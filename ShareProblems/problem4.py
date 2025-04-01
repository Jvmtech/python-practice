# Create a program that lets users add, remove, and view items in a shopping cart stored as a list.
cart = []

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        cart.append(item)
        print("Item added to cart.")
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print("Item removed from cart.")
        else:
            print("Item not found in cart.")
    elif choice == "3":
        print("Cart contents:")
        for item in cart:    
            print(item)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")  