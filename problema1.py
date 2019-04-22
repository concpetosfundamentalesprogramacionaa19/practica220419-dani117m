"""
archivo: problema1.py
ejemplo de lenguaje Python
autor:dani117m
"""

horas = input("Ingrese las horas trabajasdas:	")
v_horas = input("Ingrese el valor por hora:	")

valor_t = int(horas) * int(v_horas)
descuento = float(valor_t) * 0.10 

print("Su sueldo mensual es: %.1f\nEl descuento  del seguro social fue %.1f" % (valor_t,descuento))