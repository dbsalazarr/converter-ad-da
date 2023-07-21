import random

def generate_numbers(quantity_numbers, min_range, max_range):
    list_numbers = []
    for _ in range( quantity_numbers ) :
        list_numbers.append( random.randint(min_range, max_range ))
    
    return list_numbers

def convert_n_bits( quantity_bits) :
    pass

"""
    TODO: Fix the problem to convert the zero to zero in binary
"""
def decimal_to_binary( number ) :
    number = abs(number)
    binary_number = ""
    residuo = 0
    if number == 0 :
        binary_number = "0"
    else :
        while number > 0 :
            residuo = number % 2
            number //= 2
            binary_number += str(residuo)
    # Invert the array
    binary_number = binary_number[::-1] 
    return binary_number

def main() :
    print(" DCB DECIMAL CONVERT TO BINARY ")
    
    numbers_to_binary = []
    numbers_decimal = generate_numbers(10, 0, 4)
    for number in numbers_decimal :
        numbers_to_binary.append( decimal_to_binary(number) )

    print(" NUMBERS IN DECIMAL ")
    print(numbers_decimal)
    print(" NUMBERS IN BINARY ")
    print(numbers_to_binary)

if __name__ == "__main__" :
    main()