from time import sleep

print('Welcome to the Pet Microchip Lookup!')
sleep(2)
print("""Enter the microchip number below. Please look at the microchip number carefully. 
Check that number 1's are not lowercase l's, etc.""")
sleep(5)
microchip_number = input('Microchip number: ')

length_of_number = len(microchip_number)
print(f'Microchip number contains {length_of_number} characters.')

first_three_digits = microchip_number[:3]
if first_three_digits == '981':
    print('Datamars, PetLink')
elif first_three_digits == '985':
    print('HomeAgain')
elif first_three_digits == '977':
    print('AVID')