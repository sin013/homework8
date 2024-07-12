first = int(input("число"))
second = int(input("число"))
third = int(input("число"))
if first==second==third:
    print(1)
elif first == second or second == third or first == third:
    print(2)
else:print(0)