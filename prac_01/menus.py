menu = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(menu)
choice = input(">>>")
while choice != "Q":
    if choice != "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>>")
print("finished.")
