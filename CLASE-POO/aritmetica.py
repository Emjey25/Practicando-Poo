
class Aritmetica():
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f"El resultado de la suma es: {resultado}")

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f"El resultado de la resta es: {resultado}")

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f"El resultado de la multiplicación es: {resultado}")

    def dividir(self):
        if self.operando2 == 0:
            print("Error: No se puede dividir entre 0")
        else:
            resultado = self.operando1 / self.operando2
            print(f"El resultado de la división es: {resultado}")

# programa principal
if __name__ == "__main__":
    print("-----------Introduce dos números para realizar las operaciones aritméticas objeto 1-------------")
    operando1 = float(input("Introduce el primer número: "))
    operando2 = float(input("Introduce el segundo número: "))
    aritmetica = Aritmetica(operando1, operando2)
    aritmetica.sumar()
    aritmetica.restar()
    aritmetica.multiplicar()
    aritmetica.dividir()
# creando el segundo objeto
    print("-----------Introduce dos números para realizar las operaciones aritméticas objeto 2-------------")
    operando1 = float(input("Introduce el primer número: "))
    operando2 = float(input("Introduce el segundo número: "))
    aritmetica2 = Aritmetica(operando1, operando2)
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.multiplicar()
    aritmetica2.dividir()