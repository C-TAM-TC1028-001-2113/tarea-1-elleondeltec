def main():
    # escribe tu código abajo de esta línea
    # Esta sección es en donde pido los datos
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    # Aquí, calculo la pendiente de la recta que exite entre los dos puntos
    m = (y2 - y1) / (x2 - x1)
    # Aquí, muestro al usuario el resultado final del cálculo de la pendiente
    print("Pendiente:", m)


if __name__ == '__main__':
    main()
