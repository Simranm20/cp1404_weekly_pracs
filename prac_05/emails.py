data = {}
userinput = None

while userinput != "":
    userinput = input("Email: ")
    temp = userinput.split('@')[0]
    temp2 = temp.split('.')
    name = " ".join(temp2).title()
    data[userinput] = name

    flag = str(input(f"Is your name {name}? (Y/N)"))
    if flag.upper() != "Y" and userinput != "":
        name = input("Name: ")
        data[userinput] = name

for email, name in data.items():
    print(f"{name} ({email})")
