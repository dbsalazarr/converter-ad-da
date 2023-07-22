import decimal_to_binary as binary

def generate_binary_numbers(quantity_numbers, min_range, max_range) :
    numbers_decimal = binary.generate_numbers(quantity_numbers, min_range, max_range)
    # * convirtiendo cada número en decimal a binario
    binary_numbers = []
    for number in numbers_decimal :
        binary_numbers.append( binary.decimal_to_binary(number) )
    return binary_numbers
    


"""
    Esta función recibe el número binario como tipo str o texto
"""
def binary_to_decimal( binary_number ) :
    decimal_number = 0
    for i in range( len(binary_number) ) :
        decimal_number += int(binary_number[i])*2**( len(binary_number) - 1 - i )
    return decimal_number


def main() :
    print(" BCD BINARY CONVERT DECIMAL ")
    binaries = generate_binary_numbers(20, 0, 15) 
    decimal_numbers = []
    for binary in binaries :
        # convert to decimal 
        decimal_numbers.append( binary_to_decimal(binary) )
    

    print(" BINARIES NUMBER ")
    print(binaries)
    print(" DECIMAL NUMBERS ")
    print(decimal_numbers)


if __name__ == "__main__" :
    main()