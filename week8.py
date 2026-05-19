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




