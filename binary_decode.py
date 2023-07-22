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
    for i in range( len(gray_code) ) :
        sum = gray_code[i] + gray_code[i + 1]
        if sum >= 2 :
            binary_number += "0"
        else :
            
    
def main():
    pass

if __name__ == "__main__" :
    main()