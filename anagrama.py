a= input("ingresa una palabra: ")
b= input("ingresa otra palabra: ")

def anagrama(a, b):
  a= "".join(sorted(a))
  b= "".join(sorted(b))
  if a == b:
    return "Es anagrama"
  return "No es anagrama"

print(anagrama(a, b))