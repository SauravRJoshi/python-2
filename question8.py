def is_prime(num1):
    for i in range(2,num1):
        if i%2 == 0:
            return True
        else:
            return False    

print(is_prime(int(input("Enter a number : "))))