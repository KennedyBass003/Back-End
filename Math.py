def prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
        return True


def fibonacci(num):
    fib_sq = []
    a, b = 0, 1
    while len(fib_sq) < num:
        fib_sq.append(a)
        a, b = b, a + b
    return fib_sq


def palindrome(i_str):
    i_str = i_str.replace(" ", "").lower()
    return i_str == i_str[::-1]


def save():
    with open("homework.txt", "w", encoding="utf-8") as file:
    	file.write(str(mydict))


def confirm():
    confirm = input("Do you want to save?? yes / no??$$\t")
    if confirm.lower() == 'yes':
        save()
    elif confirm.lower() == 'no':
        quit()


print("A Mathematical interpreter")
operand = int(input("--Please enter a selection-- \n"
                    " 1. --Prime Numbers-- \n"
                    " 2. --Fibonacci sequence-- \n"
                    " 3. --Palindrome-- \n"
                    " Input selection$$\t"))
if operand == 1:
    try:
        prim_rep = int(input("You have selected the prime numbers. Please input a number to signify the range $$\t"))

        if prim_rep < 0:
            print("Prime numbers start from 0 and above.")
        else:
            print("Prime numbers up to", prim_rep, "are:")
            for number in range(1, prim_rep + 1):
                if prime(number):
                    print(number)
                confirm()
    except ValueError:
        print("Please enter a valid number.")

elif operand == 2:
    fib_rep = int(input("You have selected the fibonacci sequence. Please input a number to signify the range $$\t"))
    if fib_rep <= 0:
        print("Please enter a positive integer.")
    else:
        fib_sq = fibonacci(fib_rep)
        print("Fibonacci Sequence:")
        for y in fib_sq:
            print(y)
        confirm()
elif operand == 3:
    pal_rep = input("You have selected the Palindrome.Please input a word to evaluate$$ \t ")

    if palindrome(pal_rep):
        print(pal_rep + " is a palindrome")
    else:
        print(pal_rep + " is not a palindrome.")
        confirm()
elif operand > 3:
	print('Invalid Selection')



