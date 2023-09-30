import time
import re

# Define a dictionary of microchip brands and their associated information
microchip_brands = {
    "HomeAgain": {
        "Manufacturer": "HomeAgain",
        "Frequency": "125kHz",
        "Contact Phone Number": "1-800-422-5361"
    },
    "Banfield": {
        "Manufacturer": "Banfield",
        "Frequency": "125kHz",
        "Contact Phone Number": "1-800-722-7381"
    },
    "Datamars, PetLink": {
        "Manufacturer": "Datamars",
        "Frequency": "125kHz",
        "Contact Phone Number": "1-800-289-7387"
    },
    "AVID": {
        "Manufacturer": "AVID",
        "Frequency": "125kHz",
        "Contact Phone Number": "1-800-828-2843"
    },
    "24 PetWatch": {
        "Manufacturer": "24 PetWatch",
        "Frequency": "125kHz",
        "Contact Phone Number": "1-800-738-7297"
    },
    "AKC Reunite": {
        "Manufacturer": "AKC Reunite",
        "Frequency": "125kHz",
        "Contact Phone Number": "1-800-252-7387"
    }
}

# Print a welcome message
def print_welcome():
    print("Welcome to the Pet Microchip Lookup!")
    time.sleep(2)
    print("Enter the microchip number below. Please look at the microchip number carefully.")
    time.sleep(5)

# Print the results of the microchip lookup
def print_results(microchip_number, brand):
    print(f"The brand of your pet's microchip is {brand}.")
    time.sleep(1)
    print(f"The manufacturer is {microchip_brands[brand]['Manufacturer']}.")
    time.sleep(1)
    print(f"The chip's frequency is {microchip_brands[brand]['Frequency']}.")
    time.sleep(1)
    print(f"Please call {microchip_brands[brand]['Contact Phone Number']} for more information regarding your pet's microchip.")
    time.sleep(2)

# Get the microchip brand
def get_microchip_brand(microchip_number):
    length_of_number = len(microchip_number)

    first_three_digits = microchip_number[:3]

    if length_of_number == 15:
        if microchip_number[:8] == "98101000":
            brand = "Banfield"
        elif first_three_digits == "981":
            brand = "Datamars, PetLink"
        elif first_three_digits == "985":
            brand = "HomeAgain"
        elif first_three_digits == "977":
            brand = "AVID"
        elif first_three_digits == "982":
            brand = "24 PetWatch"
        elif first_three_digits == "956":
            brand = "AKC Reunite"
    elif length_of_number == 10:
        if re.match(r"4\w+", microchip_number):
            brand = "HomeAgain"
        elif re.match(r"0A1\w+", microchip_number):
            brand = "24 PetWatch"
        elif re.match(r"00\w+", microchip_number):
            brand = "AKC Reunite"
        elif re.match(r"0D0D\w+", microchip_number):
            brand = "Banfield"
        else:
            brand = "AVID"
    elif length_of_number == 9:
        brand = "AVID"
    else:
        print("Number does not match any chip format.")
        time.sleep(1)
        print("Please double check that the correct characters were inputted.")
        time.sleep(2)
        return None
