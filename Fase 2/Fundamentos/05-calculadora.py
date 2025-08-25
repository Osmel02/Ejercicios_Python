# Definir operaciones matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def potencia(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Error: módulo por cero"
    return a % b

# Función calculadora que recibe operaciones como argumentos
def calculadora(a, b, operacion):
    """
    Ejecuta una operación matemática sobre dos números
    
    Args:
        a (float): Primer número
        b (float): Segundo número  
        operacion (function): Función que realiza la operación
    
    Returns:
        Resultado de la operación
    """
    return operacion(a, b)

# Diccionario de operaciones disponibles
operaciones = {
    '+': suma,
    '-': resta, 
    '*': multiplicacion,
    '/': division,
    '**': potencia,
    '%': modulo
}

# Ejemplos de uso
if __name__ == "__main__":
    # Uso directo
    resultado1 = calculadora(10, 5, suma)
    resultado2 = calculadora(10, 5, multiplicacion)
    
    print(f"10 + 5 = {resultado1}")  # 15
    print(f"10 * 5 = {resultado2}")  # 50
    
    # Calculadora interactiva
    print("\n--- Calculadora Interactiva ---")
    print("Operaciones disponibles: +, -, *, /, **, %")
    
    try:
        num1 = float(input("Primer número: "))
        operador = input("Operador: ")
        num2 = float(input("Segundo número: "))
        
        if operador in operaciones:
            resultado = calculadora(num1, num2, operaciones[operador])
            print(f"Resultado: {num1} {operador} {num2} = {resultado}")
        else:
            print("Operador no válido")
            
    except ValueError:
        print("Error: Ingresa números válidos")