import decimal_to_binary as binary
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

def main():
    binary_numbers = []
    numbers_gray = []
    binary_decode = []
    for i in range(0, 16) :
        number_binary = binary.convert_n_bits(4, binary.decimal_to_binary(i) )
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

if __name__ == "__main__" :
    main()