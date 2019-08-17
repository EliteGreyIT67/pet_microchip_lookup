from time import sleep
import re

print('Welcome to the Pet Microchip Lookup!')
sleep(2)
print("""Enter the microchip number below. Please look at the microchip number carefully. 
Check that number 1's are not lowercase l's, etc.""")
sleep(5)
microchip_number = input('Microchip number: ')

length_of_number = len(microchip_number)
print(f'Microchip number contains {length_of_number} characters.')

first_three_digits = microchip_number[:3]

if length_of_number == 15:
    if microchip_number[:8] == '98101000':
        print('Banfield')
    elif first_three_digits == '981':
        print('Datamars, PetLink')
    elif first_three_digits == '985':
        print('HomeAgain')
    elif first_three_digits == '977':
        print('AVID')
    elif first_three_digits == '982':
        print('24 PetWatch')
    elif first_three_digits == '956':
        print('AKC Reunite')
elif length_of_number == 10:
    if re.match(r'4\d+', microchip_number):
        print('HomeAgain')