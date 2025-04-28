import time
import re

# Define a dictionary of microchip brands and their associated information
MICROCHIP_BRANDS = {
    "HomeAgain": {"Manufacturer": "HomeAgain", "Frequency": "125kHz", "Contact Phone Number": "1-800-422-5361"},
    "Banfield": {"Manufacturer": "Banfield", "Frequency": "125kHz", "Contact Phone Number": "1-800-722-7381"},
    "Datamars, PetLink": {"Manufacturer": "Datamars", "Frequency": "125kHz", "Contact Phone Number": "1-800-289-7387"},
    "AVID": {"Manufacturer": "AVID", "Frequency": "125kHz", "Contact Phone Number": "1-800-828-2843"},
    "24 PetWatch": {"Manufacturer": "24 PetWatch", "Frequency": "125kHz", "Contact Phone Number": "1-800-738-7297"},
    "AKC Reunite": {"Manufacturer": "AKC Reunite", "Frequency": "125kHz", "Contact Phone Number": "1-800-252-7387"},
}


def print_welcome():
    """Print a welcome message."""
    print("Welcome to the Pet Microchip Lookup!")
    time.sleep(2)
    print("Enter the microchip number below. Please look at the microchip number carefully.")
    time.sleep(5)


def print_results(brand):
    """Print the results of the microchip lookup."""
    if brand not in MICROCHIP_BRANDS:
        print("Brand information not found.")
        return

    brand_info = MICROCHIP_BRANDS[brand]
    print(f"The brand of your pet's microchip is {brand}.")
    time.sleep(1)
    print(f"The manufacturer is {brand_info['Manufacturer']}.")
    time.sleep(1)
    print(f"The chip's frequency is {brand_info['Frequency']}.")
    time.sleep(1)
    print(f"Please call {brand_info['Contact Phone Number']} for more information regarding your pet's microchip.")
    time.sleep(2)


def get_microchip_brand(microchip_number):
    """Determine the brand of the microchip based on its number."""
    length_of_number = len(microchip_number)
    first_three_digits = microchip_number[:3]
    patterns = {
        15: {
            "98101000": "Banfield",
            "981": "Datamars, PetLink",
            "985": "HomeAgain",
            "977": "AVID",
            "982": "24 PetWatch",
            "956": "AKC Reunite",
        },
        10: {
            r"^4": "HomeAgain",
            r"^0A1": "24 PetWatch",
            r"^00": "AKC Reunite",
            r"^0D0D": "Banfield",
        },
        9: "AVID",
    }

    if length_of_number == 15:
        for prefix, brand in patterns[15].items():
            if microchip_number.startswith(prefix):
                return brand
    elif length_of_number == 10:
        for regex, brand in patterns[10].items():
            if re.match(regex, microchip_number):
                return brand
        return "AVID"  # Default for unrecognized 10-digit numbers
    elif length_of_number == 9:
        return patterns[9]
    else:
        print("Number does not match any chip format.")
        time.sleep(1)
        print("Please double-check that the correct characters were inputted.")
        time.sleep(2)
        return None


# Main execution flow
if __name__ == "__main__":
    print_welcome()
    microchip_number = input("Enter the microchip number: ")
    brand = get_microchip_brand(microchip_number)
    if brand:
        print_results(brand)