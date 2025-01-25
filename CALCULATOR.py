def add(n1, n2):
    return n1 + n2
def multiply(n1,n2):
    return n1*n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2

work_with_previous = 'n'
result = 0
operations = {'+':add,'-':subtract,'*':multiply,'/':divide}
while True:
    if result == 0 and work_with_previous == 'n':
        num1 = int(input("enter the first number : \n"))
    else:
        num1 = result
    operation = input("enter the operation to perform : \n")
    num2 = int(input("enter the next number : \n"))
    result = operations[operation](num1,num2)
    print(result)
    work_with_previous = input("if you want to continue with the previous result press y otherwise n")
    if work_with_previous == 'n':
        result = 0




