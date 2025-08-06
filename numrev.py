n = int(input("Enter a number: "))
revn = 0

while n > 0:
    digit = n % 10
    revn = revn * 10 + digit
    n = n // 10


print("Reversed number:", revn)