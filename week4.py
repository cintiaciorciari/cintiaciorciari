
#comparison operators

age=20
print(age >= 18)  # true - is the person an adult?

price = 9.99
budget = 10.00
print(price<= budget) #true- can we afford it?

password= "abc123"
print(password == "abc123") #true
print(password == "ABC123")#false-case sensitive

score= 85
print(score==100)#false
print(score !=100)#true

#logical operators

age=25
has_ticket= True
is_raining= False

#and :ambos deben ser verdaderos
print(age >= 18 and has_ticket) #true

#or: al menos uno debe ser verdadero
print(age >=18 or has_ticket) #true
print(age < 18 or has_ticket) #true

#not: cambia verdadero a falso o viceversa
print(not is_raining) # True
print(not has_ticket) # False


# condiciones 
#if: se ejecuta si es verdadera
#elif: se ejecuta si la anterior fue falsa

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")
    
 #else: si ninguna se cumple   
else:
    print("You are a minor.")



#Combining Conditions

age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? (yes/no) ")
if age >= 18 and has_ticket == "yes":
  print("Welcome! Enjoy the show.")
elif age >= 18 and has_ticket != "yes":
  print("You need a ticket to enter.")
elif age < 18 and has_ticket == "yes":
  print("Sorry, this event is 18+.")
else:
  print("You need to be 18+ and have a ticket.")

#Nested conditionals

age=int(input("How old are you?") )
if age >= 18:
    country= input ("Which country are you from?")
    if country == "Denmark":
        print("You can vote in Danish elections!")
    else:
        print("You are an adult, but not eligible for Danish elections.")
else:
  print("You are too young to vote.")


#shorthand condicionals



  


