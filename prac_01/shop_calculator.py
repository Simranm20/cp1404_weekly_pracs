items = int(input("Number of items: "))
total_price = 0
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
for i in range(1, items + 1):
    b = float(input("Price of item: "))
    total_price = total_price + b
if total_price > 100:
    total_price = 0.9*total_price
print("Total Price for 3 items is $", total_price)
