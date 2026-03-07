data = input("Enter number: ")
print(f"You entered: {data}")
print(type(data))
num = int(data)

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")