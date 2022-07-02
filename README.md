# CalcDesc

Este programa sirve para calcular el precio final según el precio original y el descuento que se le proporcione.


## Usage/Examples

- Linux:
    ```bash
    chmod +x calcdes.py
    ./calcdes.py # Corre el programa de forma interactiva.
    ./calcdes.py -p [PRECIO] -d [DESCUENTO] # Corre el programa según el precio y el descuento en una sola línea.
    ```


## Features

- Se encuentra optimizado.
- Uso interactivo y en una sola línea.

## Optimizations

- Se optimizó la función `discount` tal que permite obtener el siguiente rendimiento. (Prueba mediante Google Colaboratory)

```python
def discount(precio: float, desc: float) -> float:
    return precio - (precio * 0.01 * desc)

if __name__ == "__main__":
  %timeit -n100000000 discount(20000, 50)
```
>Output:
```python
    100000000 loops, best of 5: 172 ns per loop
```

