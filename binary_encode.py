import decimal_to_binary as dtb

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

# Codificando la señal a tratar
def encode( value, quantity_bits ) :
    binary_value = ""
    if value >= 12 :
        binary_value = dtb.decimal_to_signed_binary(15, quantity_bits)
    elif value >= 11.25 :
        binary_value = dtb.decimal_to_signed_binary(15, quantity_bits)
    elif value >= 10.5 :
        binary_value = dtb.decimal_to_signed_binary(14, quantity_bits)
    elif value >= 9.75 : 
        binary_value = dtb.decimal_to_signed_binary(13, quantity_bits)
    elif value >= 9 :
        binary_value = dtb.decimal_to_signed_binary(12, quantity_bits)
    elif value >= 8.25 :
        binary_value = dtb.decimal_to_signed_binary(11, quantity_bits)
    elif value >= 7.5 :
        binary_value = dtb.decimal_to_signed_binary(10, quantity_bits)
    elif value >= 6.75 :
        binary_value = dtb.decimal_to_signed_binary(9, quantity_bits)
    elif value >= 6 :
        binary_value = dtb.decimal_to_signed_binary(8, quantity_bits)
    elif value >= 5.25 :
        binary_value = dtb.decimal_to_signed_binary(7, quantity_bits)
    elif value >= 4.5 :
        binary_value = dtb.decimal_to_signed_binary(6, quantity_bits)
    elif value >= 3.75 :
        binary_value = dtb.decimal_to_signed_binary(5, quantity_bits)
    elif value >= 3 :
        binary_value = dtb.decimal_to_signed_binary(4, quantity_bits)
    elif value >= 2.25 :
        binary_value = dtb.decimal_to_signed_binary(3, quantity_bits)
    elif value >= 1.5 :
        binary_value = dtb.decimal_to_signed_binary(2, quantity_bits)
    elif value >= 0.75 :
        binary_value = dtb.decimal_to_signed_binary(1, quantity_bits) 
    elif value >= 0 :
        binary_value = dtb.decimal_to_signed_binary(0, quantity_bits) 
    elif value >= -0.75 :
        binary_value = dtb.decimal_to_signed_binary(0, quantity_bits) 
    elif value >= -1.5 :
        binary_value = dtb.decimal_to_signed_binary(-1, quantity_bits) 
    elif value >= -2.25 :
        binary_value = dtb.decimal_to_signed_binary(-2, quantity_bits) 
    elif value >= -3 :
        binary_value = dtb.decimal_to_signed_binary(-3, quantity_bits) 
    elif value >= -3.75 :
        binary_value = dtb.decimal_to_signed_binary(-4, quantity_bits) 
    elif value >= -4.5 :
        binary_value = dtb.decimal_to_signed_binary(-5, quantity_bits) 
    elif value >= -5.25 :
        binary_value = dtb.decimal_to_signed_binary(-6, quantity_bits) 
    elif value >= -6 :
        binary_value = dtb.decimal_to_signed_binary(-7, quantity_bits) 
    elif value >=  -6.75:
        binary_value = dtb.decimal_to_signed_binary(-8, quantity_bits) 
    elif value >=  -7.5:
        binary_value = dtb.decimal_to_signed_binary(-9, quantity_bits) 
    elif value >=  -8.25:
        binary_value = dtb.decimal_to_signed_binary(-10, quantity_bits) 
    elif value >=  -9:
        binary_value = dtb.decimal_to_signed_binary(-11, quantity_bits) 
    elif value >=  -9.75:
        binary_value = dtb.decimal_to_signed_binary(-12, quantity_bits) 
    elif value >=  -10.5:
        binary_value = dtb.decimal_to_signed_binary(-13, quantity_bits) 
    elif value >=  -11.25:
        binary_value = dtb.decimal_to_signed_binary(-14, quantity_bits) 
    else :
        binary_value = dtb.decimal_to_signed_binary(-15, quantity_bits) 
    
    return binary_value

def main() :
    print("El numero en binario es: ")
    binary_numbers = []
    gray_code = []
    for i in range(0, 4) :
        binary_number = dtb.decimal_to_binary(i)
        binary_numbers.append( dtb.convert_n_bits(4, binary_number))
        gray_code.append( dtb.convert_n_bits(4, gray_encode(binary_number)) )

    print("BINARY NUMBERS")
    print( binary_numbers)
    print("GRAY CODE")
    print(gray_code)

if __name__ == "__main__" :
    main()