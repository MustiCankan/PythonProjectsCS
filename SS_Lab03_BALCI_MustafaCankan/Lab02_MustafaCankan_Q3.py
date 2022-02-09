'Lab 2 Answer 3  by Mustafa Cankan BALCI 22101761 ME'

import random

desired_dice_sum = int(input('Desired dice sum: '))

counter = 0

value = 0

while desired_dice_sum != 0:
    if desired_dice_sum < 2 or desired_dice_sum > 12:
        print('Invalid dice sum, try again...')
        print('')
        desired_dice_sum = int(input('Desired dice sum: '))
    else:
        while desired_dice_sum != value:
            counter += 1
            roll_one = random.randint(1,6)
            roll_two = random.randint(1,6)
            value = roll_one + roll_two
        print(counter,'rolls')
        counter = 0 
        value = 0
        print('')
        desired_dice_sum = int(input('Desired dice sum: '))
        
        
print('bye!')
