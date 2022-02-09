'Lab 2 Answer 2  by Mustafa Cankan BALCI 22101761 ME'

import random

input_value = input('Enter a string: ')


reverse_str = ''
while input_value != '':
    for i in input_value[::2]:
        reverse_str += i
    for i in input_value[1::2]:
        reverse_str += i
    print('new string is ' + reverse_str)
    reverse_str = ''
    print('')
    input_value = input('Enter a string: ')
        
    
      
print('done!')
    
