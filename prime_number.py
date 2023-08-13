number = int(input("Enter your number: "))
in_case = False
def prime_checker(number):
    for i in range(2, number):
        if number%i== 0:
            in_case=True
            break

    if in_case:
        print(f"{number} is not Prime")
    else: 
        print(f"{number} is Prime")
prime_checker(number)