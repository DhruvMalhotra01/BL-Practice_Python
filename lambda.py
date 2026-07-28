str1 = "string"
upper = lambda string : string.upper()
print(upper(str1))

findMax = lambda a,b,c : max(a,b,c)
print(findMax(1,3,2))

numbers = [29, 45, 32, 49, 37]

doubled = list(map(lambda x: x * 2, numbers))

print(doubled)