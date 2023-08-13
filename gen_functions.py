import numpy as np

def generate_sin(amplitud, freq_angular, dominio) :
    """
        Función para generar una función senoidal de forma generica
        Args : 
            amplitud (int) : Define la amplitud de la señal senoidal
            freq_angular (float) : Frecuencia angular expresada en rad/s
            dominio : intervalo de valores en el tiempo al cual se asigna un determinado valor de voltaje
        Returns :
            list : Retorna el rango o correspodiente univoco a cada valor en el tiempo mediante la relación matematica definida (sin)
    """
    rango = amplitud*np.sin(freq_angular*dominio)
    return rango

def main() :
    x = np.arange(0, 25)
    y = generate_sin(12, 15.1*10**-6, x)
    print(y)
    

if __name__ == "__main__" :
    main