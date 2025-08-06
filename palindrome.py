stra = str(input())
# using builtin function
if  stra ==stra[::-1] :
    print("palindrome")
else:
    print("Not palindrome")

# without using builtin funtions


n = len(stra)
flag = True
for i in range(n // 2) :
    if stra[i] != stra[n - i - 1]:
        flag = False

if flag :
    print("Palindrome")
else :
    print("Not Palindrome")
       