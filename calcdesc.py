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
    
try:
    if args.precio:
        x = int(args.precio)
    else:
        x = int(input("Ingrese el precio del producto: "))
    if args.descuento:
        y = int(args.descuento)
    else:
        y = int(input("Ingrese el descuento: "))    

    if (x >= 0 and y >=0):        
        def discount(x, y):
            if (x % 2 == 0):
                ans = int(abs(x-(x*(y/100))))
            else:
                ans = float(abs(x-(x*(y/100))))
            print(f'El precio real de ${x} con {y}% de descuento es ${ans}')    

        discount(x, y)
    else:
        print("El precio y el descuento deben de ser positivos.")
except KeyboardInterrupt:
    print("\nHas detenido el programa.")
except ValueError:
    print("\nIngrese solo valores numéricos.")
