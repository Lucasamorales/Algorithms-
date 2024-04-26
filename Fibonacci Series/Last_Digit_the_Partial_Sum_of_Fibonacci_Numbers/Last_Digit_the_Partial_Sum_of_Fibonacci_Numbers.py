"""
Last Digit of the Partial Sum of Fibonacci
Numbers Problem
Compute the last digit of Fm + Fm+1 + ··· + Fn.
Input: Integers m ≤ n.
Output: The last digit of Fm +
Fm+1 + ··· + Fn.
2 + 3 + 5 + 8 + 13 = 31
Input format. Integers m and n.
Output format. (Fm + Fm+1 + ··· + Fn) mod 10.
Constraints. 0 ≤ m ≤ n ≤ 1014
.
"""

"""
1. Función last_digit_of_fibonacci(n)
Esta función calcula el último dígito del n-ésimo número de Fibonacci. 
Utiliza un enfoque iterativo simple para calcular los números de Fibonacci hasta n 
y solo guarda el último dígito (usando (previous + current) % 10 para asegurar que solo se mantenga el último dígito,
 lo cual es suficiente dado que estamos interesados en el módulo 10).

Variables previous y current: Estas variables almacenan los dos últimos números de Fibonacci calculados.
Inicialmente, previous es 0 (F0) y current es 1 (F1).
Bucle for: Este bucle itera desde 2 hasta n, calculando cada nuevo número de Fibonacci y actualizando previous y current en cada paso.
El resultado final en current será el último dígito de F_n.
2. Función last_partial_digit_of_fibo(m, n)
Esta función calcula el último dígito de la suma de los números de Fibonacci desde F_m hasta F_n.
 Utiliza la función last_digit_of_fibonacci para obtener los dígitos necesarios y aplica un truco matemático basado en el período de Pisano para reducir la cantidad de cálculos:

Manejo del período de Pisano: Sabemos que los últimos dígitos de los números de Fibonacci se repiten cada 60 términos cuando se considera módulo 10. Esto se utiliza para reducir cualquier índice n o m al equivalente en su ciclo actual del período de Pisano.
m_mod es calculado como (m + 1) % 60 y n_mod como (n + 2) % 60 para ajustar correctamente el rango de suma a los índices requeridos para usar la relación de suma de Fibonacci, donde la suma de Fibonacci hasta F_n es F_(n+2) - 1.
Si n_mod < m_mod, ajustamos n_mod sumando 60 para manejar correctamente los casos donde el intervalo cruza el final de un ciclo de Pisano.
Cálculo de la suma: La suma de los números de Fibonacci desde F_m hasta F_n se calcula como la diferencia de F_(n+2) menos F_(m+1), aprovechando la fórmula de la suma acumulada de Fibonacci. Usamos la función last_digit_of_fibonacci para obtener los últimos dígitos de F_(m+1) y F_(n+2), y luego restamos estos dos resultados.
La variable last_digit almacena este resultado, y se ajusta para asegurar que sea un número no negativo tomando el módulo 10 nuevamente y ajustando en caso de que el resultado inicial sea negativo.
"""


def last_partial_digit_of_fibo(m, n):
    # function to calculate the last digit of fibonacci based on range m to n
    def last_digit_fib(n):
        if n <= 1:
            return n
        previous, current = 0, 1
        for i in range(n - 1):
            previous, current = current, (previous + current) % 10
        return current

    # Compute last digit of Fm + Fm+1 + ... + Fn using Pisano period:
    if m > n:
        return 0

    # to compute the sum from F_m to F_n:
    # you need S(m, n) = F_(n+2) - F_(m+1).
    m_mod, n_mod = (m + 1) % 60, (n + 2) % 60

    if n_mod < m_mod:
        n_mod += 60

    sum_m = last_digit_fib(m_mod) if m_mod != 0 else 0
    sum_n = last_digit_fib(n_mod)

    last_digit = (sum_n - sum_m) % 10

    return last_digit if last_digit >= 0 else last_digit + 10


if __name__ == '__main__':
    m, n = map(int, input("Enter the values of m and n separated by a space: ").split())
    print("The last digit of the sum of Fibonacci numbersfrom Fm up to Fn is:", last_partial_digit_of_fibo(m, n))



