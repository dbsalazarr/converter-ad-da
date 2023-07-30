import decimal_to_binary as binary

def gray_encode( binary ) :
    """
    Función que codifica un número binario en el código ciclico y adyacente gray
    
    Args:
        binary (string) : Se hace uso de un string para poder recorrer de manera más sencilla cada número mediante un bucle
    
    Returns :
        string : La codificación generada retornada un string

    Ejemplo del gray code

    1001 => 1101
    1111 => 1000
    0001 => 0001
    01111 => 01000
    """
    gray_code = str( binary[0] )
    for i in range ( len(binary) - 1 ) :
        if int(binary[i]) + int(binary[i+1]) >= 2:
            gray_code += "0"
        else :
            gray_code += str( int(binary[i]) + int(binary[i+1]) )
    
    return gray_code           

def main() :
    print("El numero en binario es: ")
    binary_numbers = []
    gray_code = []
    for i in range(0, 4) :
        binary_number = binary.decimal_to_binary(i)
        binary_numbers.append( binary.convert_n_bits(4, binary_number))
        gray_code.append( binary.convert_n_bits(4, gray_encode(binary_number)) )

    print("BINARY NUMBERS")
    print( binary_numbers)
    print("GRAY CODE")
    print(gray_code)

if __name__ == "__main__" :
    main()