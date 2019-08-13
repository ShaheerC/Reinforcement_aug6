def ordinal(num):
    if num == 1:
        return str(num)+"st"
    elif num == 2:
        return str(num)+"nd"
    elif num == 3: 
        return str(num)+"rd"
    elif num <= 20:
        return str(num)+"th"
    else:
        return "Please enter a number from 1 to 20!"

print(ordinal(1))
print(ordinal(2))
print(ordinal(3))
print(ordinal(4))
print(ordinal(5))
print(ordinal(21))