#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(
    description = 'Este es un programa para calcular el precio final según el precio y el descuento que se proporcionen.',
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument("-p", "--precio", help = "Indica el precio del producto.")
parser.add_argument("-d", "--descuento", help = "Indica el descuento que se le aplica al precio.")
parser.add_argument("-v", "--version", action = 'version' ,version='%(prog)s 1.0')
args = parser.parse_args()

def discount(precio, desc):
    ans = float(precio - (precio * (desc / 100)))
    return ans

try:
    if args.precio:
        precio = int(args.precio)
    else:
        precio = int(input("Ingrese el precio del producto: "))

    if args.descuento:
        desc = int(args.descuento)
    else:
        desc = int(input("Ingrese el descuento: "))    

    if (precio >= 0 and desc >=0):
        ans = discount(precio, desc)
        print(f'El precio real de ${precio} con {desc}% de descuento es ${ans}')    
    else:
        print("El precio y el descuento deben de ser positivos.")

except KeyboardInterrupt:
    print("\nHas detenido el programa.")
except ValueError:
    print("\nIngrese solo valores numéricos.")
