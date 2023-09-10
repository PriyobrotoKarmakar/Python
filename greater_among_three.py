a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a>b):
    if(b>c):
        print(f"{a}>{b}>{c}")
    elif(c>b):
        print(f"{a}>{c}>{b}")
    else:
        print(f"{a}>{b}={c}")
elif (b>a):
    if(a>c):
        print(f"{b}>{a}>{c}")
    elif(c>a):
        print(f"{b}>{c}>{a}")
    else:
        print(f"{b}>{a}={c}")
elif (c>b):
    if(b>a):
        print(f"{c}>{b}>{a}")
    elif(a>b):
        print(f"{c}>{a}>{b}")
    else:
        print(f"{c}>{a}={b}")
else:
    print(f"{a}={b}={c}")


