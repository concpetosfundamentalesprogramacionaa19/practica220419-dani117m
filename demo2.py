"""
archivo: demo2.py
ejemplo de lenguaje Python
autor:dani117m
"""
import sys 

nombre_archivo = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]
suma = int(valor1) + int(valor2) #se realiza la suma
multiplicacion = int(valor1) * int(valor2)# multiplicacion
print("La suma es: %s" % suma)
print("La multiplicacion es: %s" % multiplicacion)