from random import randint

upper_bound = int(input("Wie hoch soll die zu erratene Zahl maximal sein ? "))
secret_number = randint(0, upper_bound)

print("Es wurde soeben eine Zufallszahl zwischen 0 und " + str(upper_bound) + " generiert.")
print("Deine Aufgabe ist es zu erraten, welche Zahl es ist.")
print("Viel Erfolg")

guess = None
count = 1

while guess != secret_number:

    guess = int(input("Wähle eine Ganzzahl zwischen 0 und " + str(upper_bound) + ": "))

    if guess == secret_number:
        print("Yeah, das ist korrekt!")
    elif guess < secret_number:
        print("Die gesuchte Zahl ist größer als deine geratene Zahl!")
        count += 1
    else:
        print("Die gesuchte Zahl ist kleiner als deine geratene Zahl!")
        count += 1

print("Du hast " + str(count) + " Versuche benötigt, um die korrekte Zahl zu erraten!")
