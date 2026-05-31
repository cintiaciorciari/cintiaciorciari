

contacts = {

"Sara": {"phone": "0176 111", 
         "email": "sara@gmail.com"},
"Ahmed": {"phone": "0176 222",   
     "email": "ahmed@gmail.com"}

    }



contacts = {
    "Pedro": {},
    "Ana": {},
    "Carlos": {}
}
for name in sorted(contacts): # sorted ordena alfabeticamente
    print(name) 


if name in contacts:
    print("Contact already exists")
else:
    contacts[name] = {
        "phone","email"
    }


from datetime import datetime
datetime.now()

contacts[name] = {
    "phone": phone,
    "created": datetime.now()
}