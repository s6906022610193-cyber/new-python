column = int(input("Enter the number of colums: "))
for i in range(1,101):
    print(f"{i:3}", end=" ")
    if i % column == 0:
        print()