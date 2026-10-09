from tkinter import *
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
MORSE_LETTERS = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.",
                 "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__.."]

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
MORSE_NUMBERS = ["_____", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____."]

def convert():
    morse = []
    morse_entry.delete(0, END)
    t = list(text_entry.get().upper())

    for character in t:
        if character in LETTERS:
            character = MORSE_LETTERS[LETTERS.index(character)]
            morse.append(character)
        if character in NUMBERS:
            character = MORSE_NUMBERS[NUMBERS.index(character)]
            morse.append(character)
        if " " in t:
            morse.append(" ")
    morse_text = "".join(morse)
    morse_entry.insert(END, morse_text)

window = Tk()
window.title("Alice's Text To Morse Code Converter")
window.minsize(500, 400)

#Labels
welcome_label = Label(text="Welcome to the\nText To Morse Converter!")
welcome_label.config(font=("Palatino", 20), pady=30)
welcome_label.pack()

convert_label = Label(text="Enter your text (only letters and numbers):")
convert_label.config(font=("Palatino", 13), pady=5)
convert_label.pack()

#Entry1
text_entry = Entry(width=40)
text_entry.focus()
text_entry.pack()

#Button
button = Button(text="Convert", command=convert)
button.config(pady=10)
button.pack()

#Entry2
morse_entry = Entry(width=40)
morse_entry.pack()

window.mainloop()