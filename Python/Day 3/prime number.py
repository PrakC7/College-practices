num = int(input("Enter year="))
if num <=1:
    return False
i = 2
while i*i <= num:
    if num % i == 0:
        return True
