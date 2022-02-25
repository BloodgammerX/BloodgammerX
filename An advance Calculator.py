from logging import exception

print("Made by 'Shopan Bin Islam'")
print("This is a calculator\n")
print("Enter you operators and numbers\n")
try:
    a = float(input("Number1: "))
    c = str(input("Give operator(+,-,/,*,**,%): "))
    b = float(input("NUmber2: "))
except exception as e:
    print("Give a valied number")
    print(e)
def calculator(a,b,c):
    if c == "+":
        print(f"The answer is {a+b}")
    elif c == "-":
        print(f"The answer is {a-b}")
    elif c == "/":
        print(f"The answer is {a/b}")
    elif c == "*":
        print(f"The answer is {a*b}")
    elif c == "**" :
        print(f"The answer is {a**b}")
    else:
        print(f"The answer is {a%b}")
calculator(a,b,c)
def again():
    print("Do want to continue?")
    print("Enter 'y' for yes and 'n' for no")
    inpu = str(input())
    inpu.lower()
    if inpu == "y":
        a = float(input("Number1: "))
        c = str(input("Give operator(+,-,/,*,**,%): "))
        b = float(input("NUmber2: "))
        calculator(a,b,c)
        again()
    elif inpu == "n":
        print("Thanks for using my calculator!")
    else:
        print("Enter a vaild out put")
        again()

again()