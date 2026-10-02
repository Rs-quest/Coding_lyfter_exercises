print("Calculadora de etapas de vida")

name = input ("¿Cuál es tu nombre?")
lastname = input( "¿Cuál es tu apellido?")
age = int (input("¿Qué edad tienes?"))

if age <= 2:
   category = "Bebé"
   message = "eres un Bebé"
elif age <=  11:
   category = "Niño"
   message = "eres un Niño"
elif age <=  14:
   category = "Preadolescente"
   message = "eres un Preadolescente"
elif age <=  18: 
   category = "Adolescente"
   message = "eres un Adolescente"
elif age <=  25: 
   category = "Adulto joven"
   message = "eres un Adulto joven"
elif age <=  65:
   category = "Adulto"
   message = "eres un Adulto"
else:
   category = "Adulto mayor"
   message = "eres un Adulto mayor"


print(f"{name} {lastname}, tu categoría es: {category}")
print(message)