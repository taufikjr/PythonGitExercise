def multiply(num1, num2):
    return num1 * num2


print('Enter Two Desire Numbers Only To Multiply:   ')
print(' _*_ ' * 20)

frstnum = float(input('First number:  '))
scndnum = float(input('Second number: '))

result = multiply(frstnum, scndnum)
print(f"The multiplication of {frstnum} X {scndnum} is = {result}")
