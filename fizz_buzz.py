'''
This program will print the numbers from 1-100
For numbers that are multiples of 3, it will print 'Fizz'
For numbers that are multiples of 5, it will print 'Buzz'
For numbers that are multiples of 3 and 5, it will print 'FizzBuzz'
'''
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)