tasks = []

while True:
    task = input("Enter task (or type exit): ")
    if task == "exit":
        break
    tasks.append(task)

print("Your Tasks:")
for t in tasks:
    print("-", t)