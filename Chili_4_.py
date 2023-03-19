prompt = int(input("Insert a number: "))

for i in range(prompt):
    if i==0:
        continue
    if prompt%i == 0:
        print(i)