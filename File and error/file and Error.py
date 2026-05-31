# #1 #crea menu principal

# FILENAME = "contacts.txt"

# while True:

#             print("\n1. Add contact")
#             print("2. View contacts")
#             print("3. Delete contact")
#             print("4. Quit")

#             choice = input("Choose: ")

#     # ADD CONTACT
#             if choice == "1": #pedir dato

#                 name = input("Name: ")
#                 phone = input("Phone: ")
#                 email = input("Email: ")

#             duplicate = False

#             try:
#                     with open(FILENAME, "r") as file:

#                      for line in file:
#                       parts = line.strip().split(":")

#                     if parts[0].lower() == name.lower():
#                         duplicate = True
#                         break

#             except FileNotFoundError:
#                 pass

#             if duplicate:
#                 print("Contact already exists.")

#             else:
#                 with open(FILENAME, "a") as file:
#                     file.write(f"{name}:{phone}:{email}\n")

#             print("Contact saved!")

#     # VIEW CONTACTS
#             elif choice == "2":

#             try:
#                 contacts = []

#                 with open(FILENAME, "r") as file:

#                     for line in file:
#                         parts = line.strip().split(":")
#                     contacts.append(parts)

#             contacts.sort()

#             for contact in contacts:
#                 print(f"\nName: {contact[0]}")
#                 print(f"Phone: {contact[1]}")
#                 print(f"Email: {contact[2]}")

#             except FileNotFoundError:
#             print("No contacts yet.")


#     # DELETE CONTACT
#             elif choice == "3":

#             delete_name = input("Name to delete: ").lower()

#             try:
#                 new_contacts = []

#             with open(FILENAME, "r") as file:

#                 for line in file:
#                     parts = line.strip().split(":")

#                     if parts[0].lower() != delete_name:
#                         new_contacts.append(line)

#             with open(FILENAME, "w") as file:

#                 for contact in new_contacts:
#                     file.write(contact)

#             print("Contact deleted.")

#             except FileNotFoundError:
#             print("No contacts yet.")

#     # QUIT
#             elif choice == "4":
#             print("Goodbye!")
#             break

#             else:
#             print("Invalid option.")
#pedir informacion al usuario

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







