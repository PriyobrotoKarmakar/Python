#Write your code below this row 👇
#if the number is divisible by 3 = Fizz
#if the numver is divisible by 5 = Buzz
#if the number is divisible by both = FizzBuzz

for i in range (1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    
    else:
        print(i) 
