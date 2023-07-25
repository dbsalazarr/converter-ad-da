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
            0001 => 0001
            0011 => 0010
            0010 => 0011

            desarrollo 
    """
    binary_number = gray_code[0]
    for i in range( len(gray_code) - 1 ) :
        sum = int(gray_code[i]) + int(gray_code[i + 1])
        if sum >= 2 :
            binary_number += "0"
        else :
            binary_number += str( int(gray_code[i]) + int(gray_code[i + 1]) )
    return binary_number

def main():
    binary_numbers = []
    numbers_gray = []
    binary_decode = []
    for i in range(0, 16) :
        number_binary = binary.convert_n_bits(4, binary.decimal_to_binary(i) )
        binary_numbers.append( number_binary)
        
        number_gray = gray.gray_encode(number_binary)
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