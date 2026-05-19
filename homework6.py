#1 funcion 

def say_hello(name): # name is the parametro
    print ("hello, "+ name + "!") 
    print("Hello, "+ name + "!" +" welcome to RedI School")

say_hello("Sara") # is the arguments
say_hello("Ahmed")
say_hello("Maria")

#2; square es el cudrado de un numero

def square(n): #numero al cuadrado 
    return n * n

print(square(3))
print(square(5))
print(square(10))

#3 par/impar
def is_even(number):

    if  number % 2 == 0:
        return True
    else :
        return False

print(is_even(4))
print(is_even(7))
print(is_even(0))

#4
def describe_weather(temp_celsius):

    if temp_celsius < 10:
        return "cold"
    elif  temp_celsius > 10 and temp_celsius < 20 :
        return "mild"
    else:
        return "warm"

#5 default value

def greet (name, language = "English" ):   # dos parametros (name, language)
    if language == "English":
        print(f"Hello {name}!")

    elif language == "German":
        print(f"Hallo {name}!")
    elif language == "Arabic":
        print(f"Marabha {name}!")

#llamadas fueras de la funcion 
greet("Sara") # uses default: English
greet("Ahmed", "Arabic") # overrides default
greet("Maria", "German")

#6 multiplicacion 

def times_table(n): #defines la funcion con un parametro 
 
 for i in range(1,11): #loops
   
   print(n,"x",i,"=",n*i) # hacer la multiplicacion 

#llamar la funcion/argumento

times_table(3) 

#7
def celsius_to_fahrenheit(celsius):

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(20))

#8
def count_down(n):
    for i in range(n,0,-1):
        print(i)
    


count_down(5) 
print("Go! 🚀 ")

#9
def print_item(item, price, quantity):
    print(f"{item} X {quantity} = {price*quantity}")


print_item("Bread", 1.5, 2)
print_item("Coffee", 2.0, 3)
print_item("Apples", 0.5, 6)

#10

def repeat_word(word,times):
    for i in range(1,times+1):
        print(f"{i} : {word}" )


repeat_word("python", 4)

#11 suma incluyendo ultimo numero

def sum_range(start,End):
    result= 0
    for i in range(start,End+1): #incluye el ultimo numero
         result += i  #suma
    return result 
    

print(sum_range(1, 5))
print(sum_range(1, 10))
print(sum_range(5, 8))   

#11 calcular calificaciones

def get_grade(score):

    if score >= 90: #condicionales
        return "A"

    elif score >= 70:
        return "B"

    elif score >= 50:
        return "C"

    else:
        return "F"


def print_result(name, score):

    grade = get_grade(score)

    print(f"{name} scored {score} — Grade: {grade}")


print_result("Sara", 92)
print_result("Ahmed", 67)
print_result("Maria", 45)

#12

def fizzbuzz(number):

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"

    elif number % 3 == 0:
        return "Fizz"

    elif number % 5 == 0:
        return "Buzz"

    else:
        return str(number) #cambia a string


for i in range(1, 21):
    print(fizzbuzz(i))

#13 
def count_vowels(word):

    count = 0

    for letter in word: #recorre la palabra

        if letter in "aeiou":
            count += 1 #suma

    return count
# 14
def final_price(price, discount_percent=0):

    discount_amount = price * discount_percent / 100

    final = price - discount_amount

    return final


def print_deal(item, price, discount=0):

    new_price = final_price(price, discount)

    print(f"{item}: €{price} → after {discount}% off: €{new_price}")

    print_deal("Coffee", 16.0, 10)
    print_deal("Bread", 3.0) 





   



