in_stock = {"apple", "watermelon", "strawberry"}
out_of_stock = {"banana", "orange", "guava"}

# Function to update stock
def update_stock(fruit, status):
    fruit = fruit.lower()

    if status == "in":
        in_stock.add(fruit)
        out_of_stock.discard(fruit)
        print(f"\n{fruit.title()} has been added to in-stock.")

    elif status == "out":
        out_of_stock.add(fruit)
        in_stock.discard(fruit)
        print(f"\n{fruit.title()} has been moved to out-of-stock.")

    else:
        print("\nInvalid status.")


# Menu-driven program
while True:

    print("\n--- Fruit Store Inventory Management ---")
    print("1. Check if a fruit is in stock")
    print("2. List all items in the store")
    print("3. Update stock (add/remove item)")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":

        fruit = input("Enter the name of the fruit to check: ").lower()

        if fruit in in_stock:
            print(f"{fruit.title()} is in stock.")
        else:
            print(f"{fruit.title()} is not in stock.")

    elif choice == "2":

        all_items = in_stock.union(out_of_stock)

        print("\nThe possible items that the store keeps are:")

        for fruit in all_items:
            print(fruit.title())

    elif choice == "3":

        fruit = input("Enter the name of the fruit: ")
        status = input("Enter 'in' if the item is now in stock or 'out' if it is out of stock: ").lower()

        update_stock(fruit, status)

    elif choice == "4":

        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")