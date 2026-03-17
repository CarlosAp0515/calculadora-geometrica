pi = 3.1416


# -------------------------
# FUNCION PARA VALIDAR NUMEROS
# -------------------------

def pedir_numero(mensaje):

    while True:
        try:
            valor = input(mensaje)
            valor = valor.replace(",", ".")
            numero = float(valor)

            if numero <= 0:
                print("Error: la medida debe ser mayor que 0.")
            else:
                return numero

        except:
            print("Error: debe ingresar un número válido.")


menu = ""

while menu != "3":

    print("\nCALCULADORA GEOMETRICA")
    print("1. Figuras 2D")
    print("2. Figuras 3D")
    print("3. Salir")

    menu = input("Seleccione una opción: ")

# =====================================================
# FIGURAS 2D
# =====================================================

    if menu == "1":

        figura = ""

        while figura != "6":

            print("\nFIGURAS 2D")
            print("1. Triángulo")
            print("2. Cuadrado")
            print("3. Círculo")
            print("4. Trapecio")
            print("5. Triángulo rectángulo")
            print("6. Volver")

            figura = input("Seleccione figura: ")

# TRIANGULO
            if figura == "1":

                op = ""

                while op != "4":

                    print("\nTRIANGULO")
                    print("¿Qué quieres hallar?")
                    print("1. Área")
                    print("2. Perímetro")
                    print("3. Ángulo faltante")
                    print("4. Volver")

                    op = input("Seleccione opción: ")

                    if op == "1":

                        base = pedir_numero("Base: ")
                        altura = pedir_numero("Altura: ")

                        area = (base * altura) / 2
                        print(f"Área = {area:.4f}")

                    elif op == "2":

                        l1 = pedir_numero("Lado 1: ")
                        l2 = pedir_numero("Lado 2: ")
                        l3 = pedir_numero("Lado 3: ")

                        if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
                            print("Error: esos lados no pueden formar un triángulo.")
                        else:
                            perimetro = l1 + l2 + l3
                            print(f"Perímetro = {perimetro:.4f}")

                    elif op == "3":

                        a1 = pedir_numero("Ángulo 1: ")
                        a2 = pedir_numero("Ángulo 2: ")

                        if a1 + a2 >= 180:
                            print("Error: los ángulos no pueden sumar 180 o más.")
                        else:
                            angulo = 180 - (a1 + a2)
                            print(f"Ángulo faltante = {angulo:.4f}")

# CUADRADO
            elif figura == "2":

                op = ""

                while op != "3":

                    print("\nCUADRADO")
                    print("¿Qué quieres hallar?")
                    print("1. Área")
                    print("2. Perímetro")
                    print("3. Volver")

                    op = input("Seleccione opción: ")

                    if op == "1":

                        lado = pedir_numero("Lado: ")
                        area = lado ** 2
                        print(f"Área = {area:.4f}")

                    elif op == "2":

                        lado = pedir_numero("Lado: ")
                        perimetro = lado * 4
                        print(f"Perímetro = {perimetro:.4f}")

# CIRCULO
            elif figura == "3":

                op = ""

                while op != "4":

                    print("\nCIRCULO")
                    print("¿Qué quieres hallar?")
                    print("1. Área")
                    print("2. Perímetro")
                    print("3. Diámetro")
                    print("4. Volver")

                    op = input("Seleccione opción: ")

                    if op == "1":

                        radio = pedir_numero("Radio: ")
                        area = pi * radio ** 2
                        print(f"Área = {area:.4f}")

                    elif op == "2":

                        radio = pedir_numero("Radio: ")
                        perimetro = 2 * pi * radio
                        print(f"Perímetro ={perimetro:.4f}")

                    elif op == "3":

                        radio = pedir_numero("Radio: ")
                        diametro = 2 * radio
                        print(f"el Diámetro es igual a = {diametro:.4f}")

# TRAPECIO
            elif figura == "4":

                op = ""

                while op != "3":

                    print("\nTRAPECIO")
                    print("¿Qué quieres hallar?")
                    print("1. Área")
                    print("2. Perímetro")
                    print("3. Volver")

                    op = input("Seleccione opción: ")

                    if op == "1":

                        B = pedir_numero("Base mayor: ")
                        b = pedir_numero("Base menor: ")
                        h = pedir_numero("Altura: ")

                        if b >= B:
                            print("Error: la base menor no puede ser mayor o igual que la base mayor.")
                        else:
                            area = ((B + b) * h) / 2
                            print(f"El Área es igual = {area:.4f}")

                    elif op == "2":

                        B = pedir_numero("Base mayor: ")
                        b = pedir_numero("Base menor: ")
                        l1 = pedir_numero("Lado izquierdo: ")
                        l2 = pedir_numero("Lado derecho: ")

                        if b >= B:
                            print("Error: la base menor no puede ser mayor que la base mayor.")
                        else:
                            perimetro = B + b + l1 + l2
                            print(f"Perímetro ={perimetro:.4f}")

# TRIANGULO RECTANGULO
            elif figura == "5":

                op = ""

                while op != "4":

                    print("\nTRIANGULO RECTANGULO")
                    print("¿Qué quieres hallar?")
                    print("1. Hipotenusa")
                    print("2. Cateto")
                    print("3. Ángulo faltante")
                    print("4. Volver")

                    op = input("Seleccione opción: ")

                    if op == "1":

                        c1 = pedir_numero("Cateto 1: ")
                        c2 = pedir_numero("Cateto 2: ")

                        hip = ((c1 ** 2) + (c2 ** 2)) ** 0.5
                        print(f"Hipotenusa = {hip:.4f}")

                    elif op == "2":

                        hip = pedir_numero("Hipotenusa: ")
                        c1 = pedir_numero("Cateto conocido: ")

                        if c1 >= hip:
                            print("Error: el cateto no puede ser mayor o igual a la hipotenusa.")
                        else:
                            cateto = ((hip ** 2) - (c1 ** 2)) ** 0.5
                            print(f"Cateto = {cateto:.4f}")

                    elif op == "3":

                        angulo = pedir_numero("Ingrese un ángulo agudo: ")

                        if angulo <= 0 or angulo >= 90:
                            print("Error: el ángulo debe estar entre 0 y 90 grados.")
                        else:
                            faltante = 90 - angulo
                            print(f"El otro ángulo es ={faltante:.4f}")
            else:
                print("Opción no válida.")
# =====================================================
# FIGURAS 3D
# =====================================================

    elif menu == "2":

        figura = ""

        while figura != "5":

            print("\nFIGURAS 3D")
            print("1. Cubo")
            print("2. Cono")
            print("3. Cilindro")
            print("4. Esfera")
            print("5. Volver")

            figura = input("Seleccione figura: ")

# CUBO
            if figura == "1":

                op = ""

                while op != "3":

                    print("\nCUBO")
                    print("¿Qué quieres hallar?")
                    print("1. Área")
                    print("2. Volumen")
                    print("3. Volver")

                    op = input("Seleccione opción: ")

                    if op == "1":

                        lado = pedir_numero("Lado: ")
                        area = 6 * lado ** 2
                        print(f"Área = {area:.4}")

                    elif op == "2":

                        lado = pedir_numero("Lado: ")
                        volumen = lado ** 3
                        print(f"Volumen = {volumen:.4f}")

# CONO
            elif figura == "2":

                op = ""

                while op != "3":

                    print("\nCONO")
                    print("¿Qué quieres hallar?")
                    print("1. Área")
                    print("2. Volumen")
                    print("3. Volver")

                    op = input("Seleccione opción: ")

                    if op == "1":

                        r = pedir_numero("Radio: ")
                        g = pedir_numero("Generatriz: ")

                        if g <= r:
                            print("Error: la generatriz debe ser mayor que el radio.")
                        else:
                            area = pi * r * (r + g)
                            print(f"Área = {area:.4f}")

                    elif op == "2":

                        r = pedir_numero("Radio: ")
                        h = pedir_numero("Altura: ")

                        volumen = (pi * r ** 2 * h) / 3
                        print(f"Volumen = {volumen:.4f}")

# CILINDRO
            elif figura == "3":

                op = ""

                while op != "3":

                    print("\nCILINDRO")
                    print("¿Qué quieres hallar?")
                    print("1. Área")
                    print("2. Volumen")
                    print("3. Volver")

                    op = input("Seleccione opción: ")

                    if op == "1":

                        r = pedir_numero("Radio: ")
                        h = pedir_numero("Altura: ")

                        area = 2 * pi * r * (r + h)
                        print(f"Área = {area:.4f}")

                    elif op == "2":

                        r = pedir_numero("Radio: ")
                        h = pedir_numero("Altura: ")

                        volumen = pi * r ** 2 * h
                        print(f"Volumen ={volumen:.4f}")

# ESFERA
            elif figura == "4":

                op = ""

                while op != "3":

                    print("\nESFERA")
                    print("¿Qué quieres hallar?")
                    print("1. Área")
                    print("2. Volumen")
                    print("3. Volver")

                    op = input("Seleccione opción: ")

                    if op == "1":

                        r = pedir_numero("Radio: ")
                        area = 4 * pi * r ** 2
                        print(f"Área = {area:.4f}")

                    elif op == "2":

                        r = pedir_numero("Radio: ")
                        volumen = (4/3) * pi * r ** 3
                        print(f"Volumen ={volumen:.4f}")
        else:
            print("Opción no válida.")

    else:
        print("Opción no válida.")

print("\nPrograma finalizado.")