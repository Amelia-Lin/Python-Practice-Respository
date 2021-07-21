# define prime numbers
# get user input to know if the user wants one
# generate prime numbers
# provide next prime number or stop if user does not want any more

def isPrime(x):
    '''Check to see if a number is prime
    '''     
    if x == 2:
        return True
        
    if x % 2 == 0:
        return False
    
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
        
    return True

def generated_prime(current_prime):
    '''
    generates a new prime number
    '''
      
    next_prime = current_prime +1

    while True:
        if not isPrime(next_prime):
            next_prime += 1
        else:
            break
    return next_prime


def main():
    '''
    main logic of the app
    '''
    current_prime = 2
    want_another = True
    x = int()
    
    while True:
        answer = input('Would you like a prime number? "Y" or "N" ')
        
        if answer.lower() == 'y':
            print(current_prime)
            current_prime = generated_prime(current_prime)
        else:
            break

if __name__ == '__main__':
    main()