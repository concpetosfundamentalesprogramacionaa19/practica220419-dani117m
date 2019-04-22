"""
archivo: problema2.py
ejemplo de lenguaje Python
autor:dani117m
"""
x = input("Ingrese el valor de X")
y = input("Ingrese el valor de y")
z = input("Ingrese el valor de z")

v_m = float(x)+(float(y)/float(z))/float(x)+((float(y)/(float(z))))

print("los valores: \nx= %s \n y=%s\n  z=%s\n Dieron como resultado de \n\t m:%.2f" % (x, y, z, v_m))