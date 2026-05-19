contacts = {
    "Sara": {"phone": "555-1001", "city": "Berlin", "language": "German"},
    "Tom":  {"phone": "555-1002", "city": "Paris",  "language": "French"},  #dictionary
}

def add_contact(name, phone, city, language):
    contacts[name] = {"phone": phone, "city": city, "language": language}
    print(f"{name} was added!")    #almacenar los contactos en un dicionario anidado


def find_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found.") #buscar un contacto

def delete_contact(name):
    if name in contacts:
        del contacts[name] # elimnar el contacto
        print(f"{name} was deleted.")
    else:
        print(f"{name} not found.")

def show_all(): #loop para mostrar todos los contactos
    for name, info in contacts.items():
        print(f"{name} lives in {info['city']} — {info['phone']}")
   

contacts = {}

def add(name, phone, city, language):
    contacts[name] = {"phone": phone, "city": city, "language": language}

def find(name):
    print(contacts.get(name, "Not found"))

def delete(name):
    contacts.pop(name, "Not found")

def show():
    for name, info in contacts.items():
        print(f"{name} — {info['city']} — {info['phone']}")
  