#variable
secret_number= 42

guess = int(input("Guess the secret number: ")) #pedi el texto y lo converti en numero
difference= abs(secret_number-guess) #para calcular la diferencia (cerca/lejos) convierte 

#condiciones
if guess < secret_number:
    print("Too low! you are", difference, "away from the secret number")
elif guess > secret_number:
    print ("Too High!you are", difference, "away from the secret number")
else: print ("Correct!You guessed the secrect number!")
else: print ("Correct!You guessed the secrect number!") 










