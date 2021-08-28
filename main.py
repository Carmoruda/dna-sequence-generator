# color palette = https://paletasdecolores.com/paleta-de-colores-4264/
from tkinter import *


def complementary_strand():
    button.configure(state='disabled')

    dna_strand = original_entry.get().upper()
    complementary_nucleobases = {"A": "T", "T": "A", "C": "G", "G": "C"}
    adnc = ''.join([complementary_nucleobases[nucleobase] for nucleobase in dna_strand])

    complementary_label = Label(root, text='Complementary sequence: ')
    complementary_label.configure(bg='#bcb8ce')
    complementary_label.grid(pady=10, padx=10, row=2, column=0)

    complementary_entry = Entry(root, borderwidth=5, width=100)
    complementary_entry.grid(pady=10, padx=10, row=2, column=1)
    complementary_entry.insert(0, adnc)
    complementary_entry.configure(state='disabled')


root = Tk()
root.title("Complementary strands")
root.configure(bg='#bcb8ce')

# Create Widgets
original_label = Label(root, text='Input sequence: ')
original_label.configure(bg='#bcb8ce')
original_label.grid(pady=10, padx=10, row=0, column=0)

original_entry = Entry(root, borderwidth=5, width=100)
original_entry.grid(pady=10, padx=10, row=0, column=1)


button = Button(root, text='Generate complementary DNA strand', width=60, command=complementary_strand)
button.grid(padx=15, pady=15, row=2, column=1, columnspan=2)


root.mainloop()
