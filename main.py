import random

char_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_down = "abcdefghijklmnopqrstuvwxyz"

numbers = "0123456789"

symbols = "!@#$%&*()"

char_set = symbols + char_up + char_down + numbers

password_type = input("Dê um nome para a sua senha (vai ser usado depois como forma de identificação)\n\n")
password_size = input("A senha deve ter quantos caractéres?\n\n")

file = open('Passwords.txt', 'a')

password = "".join(random.sample(char_set, int(password_size)))

file.write(password_type + ": " + password + "\n")
print("Senha gerada: "+password)
file.close