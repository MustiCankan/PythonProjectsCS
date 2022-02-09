'Lab 2 Answer 1 by Mustafa Cankan BALCI 22101761 ME'

number_input = int(input('Enter an int: '))

print('Factors of ' + str(number_input) +':')

for i in range(1,number_input + 1):
    if number_input % i == 0 :
        if i == number_input:
            print(str(i), end='')
        else:
            print(str(i),', ', end='')
