n = 0
for i in range(1, 100):
    n = n+1
    if (i%3 == 0 and i%5 == 0):
        print('FizzBuzz' + str(n))
    elif (i%3 == 0):
        print('Fizz' + str(n))
    elif (i%5 == 0):
        print('Buzz' + str(n))
    #else:
       # print(str(n) + 'not a multiple of 3 or 5')
    
