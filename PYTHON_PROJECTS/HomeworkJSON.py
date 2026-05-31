import json #con Json se puede guardar diccionarios en un archivo

try:
    with open("contacts.json", "r") as file: #Cargar contactos desde archivo
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

name = input("Enter Name: ") #Agregar contacto
phone = input("Enter Phone: ")
email = input("Enter Email: ")

contacts[name] = {
    "phone": phone,
    "email": email
}

with open("contacts.json", "w") as file: #Guardar en JSON
    json.dump(contacts, file, indent=4)

print("Contact saved!") #Mostrar contactos
print("- Your Contacts -")

for name, info in contacts.items():
    print(f"{name}: {info['phone']}, {info['email']}")

    