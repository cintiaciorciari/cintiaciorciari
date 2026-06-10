

#The Contact Book

#1/2  Store & Add Contacts(almacena y agrega contactos)

contacts={} #creamos la agenda vacia

def add_contact(name, phone, city): #agregar contactos a la agenda
    contacts[name] = {
        "phone": phone, #dicionarion anidado
        "city": city
    }
    print(name + " added to contacts!")


add_contact("Sara", "0176 111", "Berlin")
add_contact("Ahmed", "0176 222", "Hamburg")
add_contact("Maria", "0176 333", "Munich")

#3 Step 3 & 4 — Find & Delete

def find_contact(name):
    if name in contacts:        # ¿Existe la llave "name" en el diccionario?
        info = contacts[name]   # Guarda el diccionario interno en "info"
        print("Name: " + name)
        print("Phone: " + info["phone"])
        print("City: " + info["city"])
    else:
        print(name + " not found in contacts.")

find_contact("Sara")     

#delete 

def delete_contact(name):
    if name in contacts: # existe name in contacts?
        del contacts[name]      # Borra esa llave y todo su contenido
        print(name + " deleted.")
    else:
        print(name + " not found.")

delete_contact("Ahmed")

#Step 5 & 6 — Show All & Put It Together

def show_all_contacts():
    if len(contacts) == 0:        # ¿El diccionario tiene 0 entradas?
        print("Contact book is empty!")
    else:
        print(" - All Contacts -")
        for name, info in contacts.items():   # Recorre cada par llave→valor
            print(name + " | " + info["phone"] + " | " + info["city"])
        print("--------------------")


add_contact("Sara", "0176 111", "Berlin")
add_contact("Ahmed", "0176 222", "Hamburg")
add_contact("Maria", "0176 333", "Munich")
show_all_contacts()
find_contact("Sara")
delete_contact("Ahmed")
show_all_contacts()



#4a)

def add_contact(name, phone, city): #agregar contactos a la agenda
    contacts[name] = {
        "phone": phone, #dicionarion anidado
        "city": city
    }
    print(name + " added to contacts!")

add_contact("Carla", "0176 000", "Argentina")
add_contact("Marcos", "0176 345", "Brazil")
add_contact("Emiliana", "0176 678", "Chile")
add_contact("Belen","0176 777","Colombia")

def find_contact(name):
    if name in contacts:        # ¿Existe la llave "name" en el diccionario?
        info = contacts[name]   # Guarda el diccionario interno en "info"
        print("Name: " + name)
        print("Phone: " + info["phone"])
        print("City: " + info["city"])
    else:
        print(name + " not found in contacts.")

find_contact("Marcos")


def delete_contact(name):
    if name in contacts: # existe name in contacts?
        del contacts[name]      # Borra esa llave y todo su contenido
        print(name + " deleted.")
    else:
        print(name + " not found.")

delete_contact("emiliana")

def show_all_contacts():
    if len(contacts) == 0:        # ¿El diccionario tiene 0 entradas?
        print("Contact book is empty!")
    else:
        print(" - All Contacts -")
        for name, info in contacts.items():   # Recorre cada par llave→valor
            print(name + " | " + info["phone"] + " | " + info["city"])
        print("--------------------")


add_contact("Carla", "0176 000", "Argentina")
add_contact("Marcos", "0176 345", "Brazil")
add_contact("Emiliana", "0176 678", "Chile")
add_contact("Belen","0176 777","Colombia")
show_all_contacts()
find_contact("Marcos")
delete_contact("Emiliana")
show_all_contacts()

#4b

contacts = {
    "Sara":  {"phone": "0176 111", "city": "Berlin"},
    "Ahmed": {"phone": "0176 222", "city": "Hamburg"},
    "Maria": {"phone": "0176 333", "city": "Munich"},
    "Leon":  {"phone": "0176 444", "city": "Berlin"}
}

def search_by_city(city):    #Search by City
    print("Contacts in " + city + ":")
    for name, info in contacts.items(): #recorre todos los contactos
        if info["city"] == city:   #filtra
            print(" - " + name + " | " + info["phone"])

search_by_city("Berlin")


#4c 
#cuantos contactos estan guardados?

def count_contacts():
    return len(contacts)   #len: cuenta cuantas llaves hay en un dicc

print("Total:", count_contacts())


#rastrear

# 📦 Diccionario de contactos
contacts = {}

# 🏙️ Set de ciudades únicas — empieza vacío
cities = set()

def add_contact(name, phone, city):
    # Agrega el contacto al diccionario
    contacts[name] = {
        "phone": phone,
        "city": city
    }
    # Agrega la ciudad al set
    cities.add(city)
    print(name + " added to contacts!")

def count_contacts():
    return len(contacts)

add_contact("Sara",  "0176 111", "Berlin")
add_contact("Ahmed", "0176 222", "Hamburg")
add_contact("Maria", "0176 333", "Munich")
add_contact("Leon",  "0176 444", "Berlin")   # Berlin repetido!

print("Total:", count_contacts())
print("Cities:", cities)


#Homework

#1/diccionario:country
#imprimir>loop

country = {
    "name": "Denmark",
    "capital": "Copenhagen",
    "population": 6000000,
    "language": "Danish"
}

for key, value in country.items(): #recorre
    print(key, ":", value)


#  2/  Update Contact Book (actualizar)

contacts = {
    "Sara": {
        "phone": "12345",
        "city": "Berlin"
    }
}

def update_contact(name, key, value):
    contacts[name][key] = value

update_contact("Sara", "city", "Frankfurt")

print(contacts)

#3/ letras unicas
 
def unique_letters(word):
    return set(word)

print(unique_letters("banana"))


#creamos sets
book_a = {
   "Sara", 
"Ahmed",
   "Maria"
    }

book_b = {
    "Ahmed",   
    "John",
    "Carla" 
    }

both= book_a & book_b
# Names in both books

print(both) #elementos en ambos sets, busca coincidencias

# Names only in book_a
print(book_a)#elemento solo en book_a

# All names combined
print(book_a | book_b)#une ambos sets sin repetir

  


