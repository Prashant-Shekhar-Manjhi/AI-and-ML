'''
  Let’s create a Simple Calculator that performs arithmetic operations. Create a function that performs addition, subtraction,
  multiplication, or division based on the operation parameter.

  [ parameter can have values '+', '-', '*' & '/' ]
'''

def calculator(a, b, operator):
    ans = 0
    if operator=='+':
        ans = a+b
    elif operator=='-':
        ans = a-b
    elif operator=='*':
        ans = a*b
    elif operator=='/':
        ans = a/b
    return ans

print(calculator(4,2,'+'))
print(calculator(4,2,'-'))
print(calculator(4,2,'*'))
print(calculator(4,2,'/'))