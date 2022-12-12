result = []
def divider(a, b):
 if b > 100:
  raise IndexError
 return a/b
firstnumber = float(input("Input the first number: "))
secondnumber = float(input("Input the second number: "))
res = divider(firstnumber, secondnumber)
result.append(res)

print(result)