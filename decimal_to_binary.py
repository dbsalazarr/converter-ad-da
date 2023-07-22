import random

def generate_numbers(quantity_numbers, min_range, max_range):
    """
        Esta función genera números de forma aleatoria, haciendo uso de la librería random
        
        Args : 
            quantity_numbers (int): Establece la cantida de números a generar
            min_range (int): Valor minimo para la generación de los números
            max_range (int): Valor máximo para la generación de los números
        
        Returns :
            list : Retorna una lista de números en base 10
        
    """
    list_numbers = []
    for _ in range( quantity_numbers ) :
        list_numbers.append( random.randint(min_range, max_range ))
    
    return list_numbers

def convert_n_bits( quantity_bits, number) :
    # Generar los zeros
    zeros = ""
    for _ in range( quantity_bits - len(number)) :
        zeros += "0"
    return zeros + number

def decimal_to_binary( number ) :
    """
        Función para convertir un número en base 10 a binarioa
        
        Args :
            number (int) : Numero a ser convertido a binario

        Returns :
            string : Esta función retorna un string con el valor en binario del número decimal ingresado
    """
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
    binary_5bits = []
    numbers_decimal = generate_numbers(10, 0, 40)
    for number in numbers_decimal :
        binary_number = decimal_to_binary(number)
        numbers_to_binary.append( binary_number )
        binary_5bits.append( convert_n_bits(5, binary_number) )

    print(" DECIMAL NUMBERS")
    print(numbers_decimal)
    print(" BINARY NUMBERS ")
    print(numbers_to_binary)
    print(" BINARY NUMBERS WITH 5BITS")
    print(binary_5bits)

if __name__ == "__main__" :
    main()