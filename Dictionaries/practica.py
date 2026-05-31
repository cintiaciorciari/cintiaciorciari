# #1
# country = {
#     "name": "Argentina",
#     "capital":"Buenos Aires",
#     "population": 120000000,
#     "language":"spanish"


# }

# country["provincia"]="Santa Fe" #agregar dato

# print(country)

# for key, value in country.items(): 
#     print(value)

# #2
# contacts = {
#     "Sara": {
#         "phone": 245678,
#         "city": "Berlin"
#     }
        
# }

# print(contacts)

# def update_contact(name, city, value):   
#     contacts [name][city]= value #modifica contactos 

# update_contact("Sara", "city", "frankfurt")
# print(contacts)
# #3

# def unique_letters(word):
#     return print(set(word)) #set elimina repetidos
      
# unique_letters("banana")

# book_a = {
#     "contact1":"Sara", 
#     "contact2":"Ahmed",
#     "contact3":"Maria"
#     }

# book_b = {
#     "contact1": "Ahmed",  
#     "contact2":"John",
#     "contact3":" Carla" 
#     }

# print(book_a - book_b)

#DATETIME

import datetime 
tiempo = datetime.datetime.now()
print(tiempo)