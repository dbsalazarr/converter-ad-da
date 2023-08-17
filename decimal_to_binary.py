import numpy as np
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

def generate_numbers(option, quantity_numbers, min_range, max_range) :
    """
        Función sobre cargada que agregar una opción para generar una lista de números de forma aleatoria o crear una lista ordenada de números
        option = 0 : Lista de ordenada entre el min y max
        option = 1 : Genera números de forma aleatoria
        Args : 
            option (int) : Determina la forma en como se generan los números
            quantity_numbers (int): Establece la cantida de números a generar
            min_range (int): Valor minimo para la generación de los números
            max_range (int): Valor máximo para la generación de los números
        
        Returns :
            list : Retorna una lista de números en base 10
        
    """
    list_numbers = []
    if option == 0 :
        list_numbers = np.arange(min_range, max_range)
    elif option == 1 :
        list_numbers = []
        for _ in range( quantity_numbers ) :
            list_numbers.append( random.randint(min_range, max_range ))
    else :
        list_numbers = []
    return list_numbers

      
    
def convert_n_bits( quantity_bits, number) :
    # Generar los zeros
    """
        Función para convertir un número binario de m bits a n bits siendo n > m,

        Args:
            quantity_bits (int) : Cantidad de bits al cual se transformará la función
            number (str) : String con el número binario el cual se transforamara a la cantidad de bits especificados
        Returns :
            str : Retorna una cadena con el número convertido a los bits deseados
    """
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

def decimal_to_signed_binary( number, quantity_bits ) :
    """
        Función para convertir un número decimal a un número binario con signo
        La función agrega un cero o uno a la magnitud de número si es positivo o negativo respectivamente.

        Args :
            number (int) : Número decimal a ser convertido
            quantity_bits (int) : Determinar la cantidad de bits con la cual se desea representar el número
        
            Returns
                string : Retorna el número binario con signo
    """
    value = abs(number)
    signed_binary = ""
    signed_binary = convert_n_bits(quantity_bits, decimal_to_binary(value))
    if number >= 0 : 
        signed_binary = "0" + signed_binary
    else :
        signed_binary = "1" + signed_binary

    return signed_binary

def main() :
    print(" DCB DECIMAL CONVERT TO BINARY ")
    
    numbers_to_binary = []
    binary_5bits = []
    numbers_decimal = generate_numbers(1, 10, 0, 40)
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

    print("============================================")
    print(" Signed Binary ")
    print("============================================")
    signed_numbers = generate_numbers(0,32,-15, 16)
    signed_binary_numbers = []
    for number in signed_numbers :
        signed_binary_numbers.append( decimal_to_signed_binary(number, 4) )
    print("DECIMAL NUMBERS WITH SIGN")
    print(signed_numbers)
    print("Binary numbers with sign")
    print(signed_binary_numbers)
    

if __name__ == "__main__" :
    main()