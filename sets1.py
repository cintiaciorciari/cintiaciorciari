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