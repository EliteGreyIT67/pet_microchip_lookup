import sleep

print('Welcome to the Pet Microchip Lookup!')
print("""Please enter the microchip number below. Please look at the microchip number carefully. 
Check that number 1's are not lowercase l's, etc.""")
microchip_number = input('Microchip number: ')

length_of_number = len(microchip_number)
print(f'Microchip number contains {length_of_number} characters.')