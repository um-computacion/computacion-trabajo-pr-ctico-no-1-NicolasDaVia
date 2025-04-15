def decimal_a_romano(numero: int) -> str:
    if not 1 <= numero <= 3999:
         raise ValueError("El valor numerico debe estar entre 1 y 3999 ")
    valores = [(1000,"M"), (900,"CM"), (500,"D"), (400,"CD"),
    (100,"C"), (90,"XC"), (50,"L"), (40,"XL"),
    (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")]
    resultado = ""
    for valor, simbolo in valores:
         while numero >= valor:
              resultado += simbolo
              numero -= valor
    return resultado

if __name__ == "__main__":
     try:
          n = int(input("Introduzca numero decimal "))
          print (decimal_a_romano(n))
     except ValueError as e:
          print("Introduzca valor valido")
