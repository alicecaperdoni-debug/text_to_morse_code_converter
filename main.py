from tkinter import *
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
MORSE_LETTERS = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.",
                 "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__.."]

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
MORSE_NUMBERS = ["_____", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____."]

def convert(text):
    morse = []
    for character in text:
        if character in LETTERS:
            character = MORSE_LETTERS[LETTERS.index(character)]
            morse.append(character)
        if character in NUMBERS:
            character = MORSE_NUMBERS[NUMBERS.index(character)]
            morse.append(character)
        if " " in text:
            morse.append(" ")
    return "".join(morse)

def keep_converting():
    original_text = list(input("Enter your text (only letters and numbers):").upper())

    morse_text = convert(original_text)
    print(morse_text)

# window = Tk()
# window.title("Alice's Text To Morse Code Converter")
# window.minsize(500, 400)
#
# #TODO-4 Fare estetica con Tkinter
# welcome_label = Label(text="Welcome to the Text To Morse Converter!")
# welcome_label.config(font=("Palatino", 20))
# welcome_label.grid(column=1, row=1)

new_conversion = True
keep_converting()

while new_conversion:
    new_translation = input("Do you want to translate again? (y/n)").lower()
    if new_translation == "y":
        keep_converting()
    else:
        print("Goodbye!")
        break

#TODO-3 Chiedi se l'utente vuole tradurre altro (sì:riparti, no:ciao - Tkinter -> chiudi finestra)











# window.mainloop()