import decimal_to_binary as dtb
import binary_to_decimal as btd
import binary_encode as gray

def gray_decode( gray_code ) :
    """
        Esta es una función para decodificar el código gray generado
        Args :
            gray_code (str) : Es el código gray generado
        Returns :
            str : Retorna el código gray decodificado (número binario original)

        Ejemplo :
            Gray => Binario

            0001 => 0001
            0011 => 0010
            0010 => 0011
            
            Gray: 0 1 1 1
            Bina: 0 1 0 1
        ANALISIS DEL PROBLEMA
        Se tiene lo siguiente
        Primer bit : es el MSB 
        Segundo bit: Suma del MSB + el 2do bit
        Tercer bit : (Suma del MSB + el 2do bit) + 3er bit
        Cuarto bit : (Suma del MSB + el 2do bit + 3er bit) + 4to bit

    """
    binary_number = gray_code[0]
    aux = gray_code[0]
    for i in range( len(gray_code) - 1) :
        if int(aux) + int(gray_code[i+1]) >= 2 :
            binary_number += "0"
            aux = "0"
        else :
            binary_number += str( int(aux) + int(gray_code[i+1]) )
            aux = str( int(aux) + int(gray_code[i+1]))
    return binary_number

def signed_binary_to_decimal( binary ) :

    """
        Función para convertir un número binario con signo a un número decimal
        Args :
            binary (str) : Número binario con signo a convertir a decimal
        Returns :
            (int) : Número en base 10 o decimal

    """
    sign = binary[0]
    number = binary[1::]
    decimal = btd.binary_to_decimal(number)
    if sign == "0" :
        return decimal
    else :
        return decimal * -1

def decode_digital_signal( bits ) :
     """
        Función para decodificar la señales codificadas
        Args :
            bits (str) :  Número binario a ser decodificado según los niveles de cuantización definidos
        Returns:
            (int) : Retorna un número decimal decodificado
     """
     analog_value = 0
     if bits == "00000" : analog_value = 0.75
     if bits == "00001" : analog_value = 1.5
     if bits == "00010" : analog_value = 2.25
     if bits == "00011" : analog_value = 3
     if bits == "00100" : analog_value = 3.75
     if bits == "00101" : analog_value = 4.5
     if bits == "00110" : analog_value = 5.25
     if bits == "00111" : analog_value = 6
     if bits == "01000" : analog_value = 6.75
     if bits == "01001" : analog_value = 7.5
     if bits == "01010" : analog_value = 8.25
     if bits == "01011" : analog_value = 9
     if bits == "01100" : analog_value = 9.75
     if bits == "01101" : analog_value = 10.5
     if bits == "01110" : analog_value = 11.25
     if bits == "01111" : analog_value = 12
     # Negative values
     if bits == "10000" : analog_value = -0.75
     if bits == "10001" : analog_value = -1.5
     if bits == "10010" : analog_value = -2.25
     if bits == "10011" : analog_value = -3
     if bits == "10100" : analog_value = -3.75
     if bits == "10101" : analog_value = -4.5
     if bits == "10110" : analog_value = -5.25
     if bits == "10111" : analog_value = -6
     if bits == "11000" : analog_value = -6.75
     if bits == "11001" : analog_value = -7.5
     if bits == "11010" : analog_value = -8.25
     if bits == "11011" : analog_value = -9
     if bits == "11100" : analog_value = -9.75
     if bits == "11101" : analog_value = -10.5
     if bits == "11110" : analog_value = -11.25
     if bits == "11111" : analog_value = -12
     return analog_value



def main():
    binary_numbers = []
    numbers_gray = []
    binary_decode = []
    for i in range(0, 16) :
        number_binary = dtb.convert_n_bits(4, dtb.decimal_to_binary(i) )
        binary_numbers.append( number_binary)
        
        number_gray = gray.gray_encode( number_binary )
        numbers_gray.append( number_gray )
        
        binary_decode.append( gray_decode( number_gray) )
        
        
    print( "BINARY NUMBERS" )
    print( binary_numbers)
    print( "GRAY CODE" )
    print( numbers_gray )
    print( " BINARY NUMBER " )
    print( binary_decode ) 

    print( " MOSTRANDO LA MAGNITUD DEL NÚMERO CON SIGNO ")
    print( signed_binary_to_decimal("000100") )

    print("DECODE DIGITAL SIGNAL")
    print(decode_digital_signal("00000"))


if __name__ == "__main__" :
    main()