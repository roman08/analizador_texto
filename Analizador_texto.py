texto = input("Ingresa un texto: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primeta letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letas1 = texto.count(letras[0])
cantidad_letas2 = texto.count(letras[1])
cantidad_letas3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letas1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letas2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letas3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)}  palabras en tu texto")

print("\n")
print("LETAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La lentra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto alrevez va a decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True: "si", False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")