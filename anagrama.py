palabra = input("ingresa una palabra: ")

def anagrama(palabra):
  palabra1 = ""
  for i in palabra:
    palabra1 = i + palabra1
  if palabra == palabra1:
     print(f"la palabra {palabra} es un anagrama")
  else:
     print(f"la palabra {palabra} no es un anagrama")

anagrama(palabra)