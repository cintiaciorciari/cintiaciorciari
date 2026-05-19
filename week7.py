#1 Indexing & Slicing

cities = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"]

print(cities[0]) #primero
print(cities[-1])#ultimo
print(cities[1:3]) 
print(cities[2:])# desde indice 2 hasta el final
print(cities[::-1]) #invertir

#2 metodos

shopping = ["milk", "eggs", "bread"]

shopping.append("butter") #agrega al final
print(shopping)

shopping.insert(1,"chesse") 
print(shopping)

shopping.remove("eggs")
print(shopping)

print(len(shopping)) #imprime cantidad de elemento
print("milk" in shopping)

shopping.sort() #ordena
print(shopping)


#Homework

#1 nombre mas largo 

def longest_name(names): #funcion 

    longest = names[0] #crea una variable

    for name in names: #loops 
        if len(name) > len(longest): #condicion comparar tamanos len():longitud,cantidad de elementos
            longest = name

    return longest #devuelve el nombre mas largo


print(longest_name(["Sara", "Ahmed", "Maria", "Leon"]))
print(longest_name(["Ana", "Bob", "Carl"]))
print(longest_name(["Li", "Mohammed", "Eva"]))


#2 intercambiar los extremos

def swap_ends(items):

    return [items[-1]] + items[1:-1] + [items[0]]
            #ultimo elemento + el medio + el primer elemento

print(swap_ends([1, 2, 3, 4, 5]))
print(swap_ends(["Berlin", "Hamburg", "Munich"]))
print(swap_ends(["a", "b"]))


#3 registro de estudiantes 

def print_top_students(students): #funcion

    for student in students: #loop

        name = student[0] #crear variable
        score = student[1]

        if score >= 70: #condicion 
            print(f"{name} — {score} ✅")


    students = [
        ("Sara", 85),
        ("Ahmed", 55),
        ("Maria", 91),
        ("Leon", 68),
        ("Fatima", 73)
]
    print_top_students(students)         


#4 rotar una lista

def rotate(items, n):

    return items[n:] + items[:n] #slicing: items[:n]first/ items[n:]end

#5 el mas freceunte 

def most_frequent(items):
    for item in items:
         items.count(item) # .count() cuenta cuantas veces aparece algo
    return item
