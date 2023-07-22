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
    print("El número en binario es: ")
    binary_number = binary.decimal_to_binary(9)
    gray_code = gray_encode( binary_number )
    print("BINARY NUMBER")
    print(binary_number)

    print("GRAY CODE")
    print(gray_code)

if __name__ == "__main__" :
    main()