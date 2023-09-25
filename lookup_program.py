from time import sleep
import re

keep_going = True


def print_welcome():
    print('Welcome to the Pet Microchip Lookup!')
    sleep(2)
    print("""Enter the microchip number below. Please look at the microchip number carefully.
Check that number 1's are not lowercase l's, etc.""")
    sleep(5)


def print_results(microchip_number, brand):
    print(f"The brand of your pet's microchip is {brand}.")
    sleep(1)

    if brand in ['HomeAgain', 'Banfield']:
        manufacturer = microchip_brands[brand]["Manufacturer_" + str(len(microchip_number)) + "_digit"]
    else:
        manufacturer = microchip_brands[brand]["Manufacturer"]

    print(f'The manufacturer is {manufacturer}.')
    sleep(1)

    if brand == 'Datamars, PetLink':
        frequency = microchip_brands[brand]["Frequency"]
    else:
        frequency = microchip_brands[brand]["Frequency_" + str(len(microchip_number)) + "_digit"]

    print(f'The chip\'s frequency is {frequency}.')
    sleep(1)

    print(f"Please call {microchip_brands[brand]['Contact Phone Number']} for more information regarding your pet\'s microchip.")
    sleep(2)


def get_microchip_brand(microchip_number):
    length_of_number = len(microchip_number)

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
        print('Number does not match any chip format.')
        sleep(1)
        print('Please double check that the correct characters were inputted.')
        sleep(2)
        return None

    return brand


if __name__ == '__main__':
    print_welcome()

    while keep_going:
        microchip_number = input('Microchip number (or Q to quit): ')
        if microchip_number == 'Q':
            break

        brand = get_microchip_brand(microchip_number)
        if brand is None:
            continue

        print_results(microchip_number, brand)

        still_keep_going = input('Do you have another number to lookup? (Y/N) ')
        if still_keep_going == 'N':
            break

    print('Thank you for using the Pet Microchip Lookup.')
