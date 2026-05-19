#1

my_profile = {

    "name": "Cintia" ,
     "age":20 , 
     "city":"Argentina" ,
     "language": "Spanish" , 
     "hobby": "circus"

     }

print(my_profile["name"]) #imprimir valores
print(my_profile["city"]) 


my_profile ["favourite_food"]="Lasagna" #agregar
print (my_profile["favourite_food"])

my_profile["age"]=36 #actualizar 
print(my_profile["age"])

if "phone" in my_profile: #verificar
    print (my_profile ["phone"])

#2 Nested Dictionaries

contacts = {
"Sara": {"phone": "0176 111", "city": "Berlin"},
"Ahmed": {"phone": "0176 222", "city": "Hamburg"}
}

contacts["Maria"] = {"phone": "0176 333", "city": "Munich"} #agregar
print(contacts["Maria"])

contacts["Sara"]["city"] = "Frankfurt" #actualizar
print(contacts["Sara"])

for name, info in contacts.items(): #loop
    print(name + " — " + info["city"])

#2

#2 Class contacts
 
class_contacts = {

    "Sara": {"phone": "0176 111", "city": "Berlin","language":"German"},
    "Pablo": {"phone": "0176 222", "city": "Roma","language": "Italian"},
    "Marcos":{"phone":"0122 333","city":"Buenos Aires","language": "spanish"} 
}

print("Sara lives in", class_contacts["Sara"]["city"])

print ( class_contacts ["Sara"]["phone"] )#Print one person’s phone number

class_contacts ["Macarena"] = {"phone": "0177 111", "city": "colombia","language":"spanish"}
print (class_contacts["Macarena"]) #agregar

for name, info in class_contacts.items(): #loop
    print(f"{name} lives in {info['city']}")


 #SETS

redi_students = {"Sara", "Ahmed", "Maria", "Leon"}
python_class = {"Sara", "Maria", "Fatima", "James"}

# UNION — everyone in either group
all_people = redi_students | python_class
print(all_people)

# {'Sara', 'Ahmed', 'Maria', 'Leon', 'Fatima', 'James'}

# INTERSECTION — only in BOTH groups
both = redi_students & python_class
print(both)
# {'Sara', 'Maria'}

# DIFFERENCE — in first but NOT in second
only_redi = redi_students - python_class
print(only_redi)
# {'Ahmed', 'Leon'}

#3

monday_class = {"Sara", "Ahmed", "Maria", "Leon", "Fatima"}
wednesday_class = {"Maria", "Leon", "James", "Sara", "Nina"}

# 1. How many students attend Monday class
print(len(monday_class)) # cuenta cuantos elementos hay

# 2. Students who attend BOTH days
print(monday_class & wednesday_class) #el símbolo & significa "dame solo lo que está en AMBOS sets"

# 3. Students who attend ONLY Monday
print(monday_class - wednesday_class) #el símbolo - significa "dame lo que está en Monday pero NO en Wednesday". Resta los que están en los dos.

# 4. All unique students across both days
print(monday_class | wednesday_class) #el símbolo | significa "dame TODO, sin repetir". Junta ambos sets en uno.

# 5. Check if Ahmed is in Wednesday's class 
if "Ahmed" in wednesday_class: #
    print("Ahmed is in Wednesday's class")
else:
    print("Ahmed is NOT in Wednesday's class")

    








