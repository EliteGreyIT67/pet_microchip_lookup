from time import sleep
import re

keep_going = True


print('Welcome to the Pet Microchip Lookup!')
sleep(2)
print("""Enter the microchip number below. Please look at the microchip number carefully. 
Check that number 1's are not lowercase l's, etc.""")
sleep(5)

while keep_going:
    microchip_number = input('Microchip number: ')

    length_of_number = len(microchip_number)
    print(f'Microchip number contains {length_of_number} characters.')
    sleep(2)

    first_three_digits = microchip_number[:3]

    if length_of_number == 15:
        if microchip_number[:8] == '98101000':
            brand = 'Banfield'
        elif first_three_digits == '981':
            brand = 'Datamars, PetLink'
        elif first_three_digits == '985':
            brand = 'HomeAgain'
        elif first_three_digits == '977':
            brand = 'AVID'
        elif first_three_digits == '982':
            brand = '24 PetWatch'
        elif first_three_digits == '956':
            brand = 'AKC Reunite'
    elif length_of_number == 10:
        if re.match(r'4\w+', microchip_number):
            brand = 'HomeAgain'
        elif re.match(r'0A1\w+', microchip_number):
            brand = '24 PetWatch'
        elif re.match(r'00\w+', microchip_number):
            brand = 'AKC Reunite'
        elif re.match(r'0D0D\w+', microchip_number):
            brand = 'Banfield'
        else:
            brand = 'AVID'
    elif length_of_number == 9:
        brand = 'AVID'
    else:
        print('Number does not match any chip format. Please double check that the correct characters were inputted.')
        sleep(2)
        continue

    print(f"{brand} is the brand of your pet's microchip.")
    sleep(2)

    microchip_brands = {'Datamars, PetLink':{'Manufacturer':'Datamars', 
                                            'Frequency':'134.2 kHz', 
                                            'Contact Phone Number':'1-877-738-5465'},
                        'HomeAgain':{'Manufacturer_15_digit':'Destron Fearing',
                                    'Manufacturer_10_digit':'Digital Angel',
                                    'Frequency_15_digit':'134.2 kHz',
                                    'Frequency_10_digit':'125 kHz',
                                    'Contact Phone Number':'1-888-466-3242'},
                        'AVID':{'Manufacturer':'AVID',
                                'Frequency_9_digit':'125 kHz', 
                                'Frequency_10_digit':'125 kHz', 
                                'Frequency_15_digit':'134.2 kHz', 
                                'Contact Phone Number':'1-800-336-2843'}, 
                        '24 PetWatch':{'Manufacturer':'Allflex', 
                                        'Frequency_15_digit':'134.2 kHz',
                                        'Frequency_10_digit':'125 kHz', 
                                        'Contact Phone Number':'1-866-597-2424'}, 
                        'AKC Reunite':{'Manufacturer':'Trovan', 
                                        'Frequency_15_digit':'134.2 kHz', 
                                        'Frequency_10_digit':'128 kHz', 
                                        'Contact Phone Number':'1-800-252-7894'}, 
                        'Banfield':{'Manufacturer_15_digit':'Datamars', 
                                    'Manufacturer_10_digit':'Unknown', 
                                    'Frequency_15_digit':'134.2 kHz', 
                                    'Frequency_10_digit':'125 kHz', 
                                    'Contact Phone Number':'1-877-567-8738'}}

    print(microchip_brands[brand])
    sleep(3)
    still_keep_going = input('Have another number to lookup? (Y/N) ')
    if still_keep_going == 'N':
        keep_going = False

