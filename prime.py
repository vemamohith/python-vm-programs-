number = int(input("Enter a number"))
if number < 2:
    print("Not a Prime Number")
else:
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")