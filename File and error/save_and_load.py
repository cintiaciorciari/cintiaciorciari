name = input("Enter Name: ")
phone = input("Enter Phone: ")

with open("contacts.txt", "a") as file:  #guardar datos con append 
    file.write(name + "," + phone + "\n")

print("Contact saved!")
print("- Your Contacts -")

 
with open("contacts.txt", "r") as file:
    for line in file:
        name, phone = line.strip().split(",")
        print(f"{name}: {phone}")