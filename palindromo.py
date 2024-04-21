palabra = input("ingresa una palabra o frase: ")

def quitarespacio(palabra):
  palabra1 =""
  for i in palabra:
    if i == " ":
      continue
    else:
      palabra1 += i
  return palabra1

def palindromo(palabra1):
  palabra2 = ""
  for i in palabra1:
    palabra2 = i + palabra2
  if palabra1 == palabra2:
     print(f"la frase {palabra} es un palindromo")
  else:
     print(f"la frase {palabra} no es un palindromo")

palabra1 = quitarespacio(palabra)
palindromo(palabra1)