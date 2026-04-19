#thisis a simple program to prim a sentece

print("Hello world!")

#definition of variables
name= "cintia"
age="36"
height="1.64"
is_student= True

#print block
print(type(name))
print(type(age))
print(type(height))
print(type(is_student)) 

#multiplicacion 
price= 19.99
quantity= 3
total = price * quantity 
print(f"total: {total}")
total= price + price + price + price
print(f"total:{total}")

#calcular ano de nacimiento
age=30
birth_year= 2026 - age
print(f"bord in:{birth_year}")

#convertir minutos a horas
minutes= 137
hours= minutes // 60
remaining= minutes % 60 
print(f"{hours}h{remaining}min")

#string operations

first="Hello"
second="World"
print(first+""+second)

#repetition
print("ha"*3)

#length
print(len("Python"))

#cambios en string
name= "   cintia   "
print(name.upper())    #mayuscula
print(name.lower())    #minuscula
print(name.strip())    #remueve espacios 
print(name.strip().capitalize()) #cambia la primer letra en mayuscula

greeting="Hello,World"
print(greeting.replace("World" ,"Python")) #rempleza la palabra

#print

name= "Cintia"
age=36
print("Hello!")
print(name)
print("My name is", name)
print("age:", age)

#input

name=input("What is your name?")
print("Hello", name)

age=input("What old are you?")
print("age",age)
print(type(age))

#type conversion

#string a int
age_str = input("How old are you?")
age = int(age_str)

#string a float

height_str = "1.64"
height = float(height_str)

number = 42
text = str(number)


name2=input("What is your name?")
age2=int(input("How old are you?"))
city=input("what city are you from?")

print(f"Nice to meet you,{name2}")
print(f"you are {age2}years old and you are from {city}")
print(f"In 10 years, you will be {age2 + 10}")



























