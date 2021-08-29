# color palette = https://paletasdecolores.com/paleta-de-colores-4264/
from tkinter import *


'''def complementary_strand():
    button.configure(state='disabled')

    dna_strand = original_entry.get().upper()
    adnc = ''.join([complementary_nucleobases[nucleobase] for nucleobase in dna_strand])

    complementary_label = Label(root, text='Complementary sequence: ')
    complementary_label.configure(bg='#bcb8ce')
    complementary_label.grid(pady=10, padx=10, row=2, column=0)

    complementary_entry = Entry(root, borderwidth=5, width=100)
    complementary_entry.grid(pady=10, padx=10, row=2, column=1)
    complementary_entry.insert(0, adnc)
    complementary_entry.configure(state='disabled')'''

root = Tk()
root.title("Complementary strands")
root.configure(bg='#bcb8ce')
root.title('DNA sequence generator')
root.iconbitmap('d:/Cosas de más/Programación/Repos/dna sequence generator/adn.ico')


def display_entries(input, complementary, reverse, reverse_complementary):
    input_entry.delete(0, END)
    input_entry.insert(0, input)
    complementary_entry.configure(state=NORMAL)
    complementary_entry.delete(0, END)
    complementary_entry.insert(0, complementary)
    complementary_entry.configure(state=DISABLED)
    reverse_entry.configure(state=NORMAL)
    reverse_entry.delete(0, END)
    reverse_entry.insert(0, reverse)
    reverse_entry.configure(state=DISABLED)
    reverse_complementary_entry.configure(state=NORMAL)
    reverse_complementary_entry.delete(0, END)
    reverse_complementary_entry.insert(0, reverse_complementary)
    reverse_complementary_entry.configure(state=DISABLED)


def dna_sequences():
    complementary_nucleobases = {"A": "T", "T": "A", "C": "G", "G": "C"}
    input_sequence = input_entry.get().upper()
    complementary_sequence = ''.join([complementary_nucleobases[nucleobase] for nucleobase in input_sequence])
    reverse_sequence = input_sequence[::-1]
    reverse_complementary_sequence = complementary_sequence[::-1]
    display_entries(input_sequence, complementary_sequence, reverse_sequence, complementary_sequence)

def rna_sequences():
    complementary_nucleobases = {"A": "U", "T": "A", "C": "G", "G": "C"}
    input_sequence = input_entry.get().upper()
    complementary_sequence = ''.join([complementary_nucleobases[nucleobase] for nucleobase in input_sequence])
    reverse_sequence = input_sequence[::-1]
    reverse_complementary_sequence = complementary_sequence[::-1]
    display_entries(input_sequence, complementary_sequence, reverse_sequence, complementary_sequence)


# Input sequence
input_label = Label(root, text='Input sequence: ')
input_label.configure(bg='#bcb8ce')
input_label.grid(pady=10, padx=10, row=0, column=0, sticky=E)
input_entry = Entry(root, borderwidth=5, width=100)
input_entry.grid(pady=10, padx=10, row=0, column=1, columnspan=2)
# complementary sequence
complementary_label = Label(root, text='Complementary sequence: ')
complementary_label.configure(bg='#bcb8ce')
complementary_label.grid(pady=10, padx=10, row=1, column=0, sticky=E)
complementary_entry = Entry(root, borderwidth=5, width=100, state=DISABLED)
complementary_entry.grid(pady=10, padx=10, row=1, column=1, columnspan=2)
# reverse sequence
reverse_label = Label(root, text='Reverse sequence: ')
reverse_label.configure(bg='#bcb8ce')
reverse_label.grid(pady=10, padx=10, row=2, column=0, sticky=E)
reverse_entry = Entry(root, borderwidth=5, width=100, state=DISABLED)
reverse_entry.grid(pady=10, padx=10, row=2, column=1, columnspan=2)
# reverse complementary sequence
reverse_complementary_label = Label(root, text='Reverse complementary sequence: ')
reverse_complementary_label.configure(bg='#bcb8ce')
reverse_complementary_label.grid(pady=10, padx=10, row=3, column=0, sticky=E)
reverse_complementary_entry = Entry(root, borderwidth=5, width=100, state=DISABLED)
reverse_complementary_entry.grid(pady=10, padx=10, row=3, column=1, columnspan=2)

# Mode
action = StringVar()

rna_action = Radiobutton(root, text='RNA', variable=action, value='RNA', bg='#bcb8ce', command=rna_sequences)
dna_action = Radiobutton(root, text='DNA', variable=action, value='DNA', bg='#bcb8ce', command=dna_sequences)
action.set('DNA')

rna_action.grid(row=5, column=1)
dna_action.grid(row=5, column=2)

mode_label = Label(root, text='Mode: ')
mode_label.configure(bg='#bcb8ce')
mode_label.grid(pady=10, padx=10, row=5, column=0, sticky=E)

#Texts
complementary_text = Text(root, height=5, width=87, bg='#bcb8ce', font=('Calibri', 10), bd=0)
complementary_text.grid(row=6, column= 1, columnspan=2)

insert_text1 = '''"In molecular biology, complementarity is a property shared between two nucleic acid sequences, such that
when they are aligned antiparallel to each other, the nucleotide bases at each position will be complementary.
Two bases are complementary if they form Watson-Crick base pairs. The degree of complementarity between
two nucleic acid strands may vary, from total complementarity to none. This tools calculates total 
complementary sequence."'''
complementary_text.insert(END, insert_text1)

complementary_DNA_text = Text(root, height=6, width=87, bg='#bcb8ce', font=('Calibri', 10), bd=0, pady=10)
complementary_DNA_text.grid(row=7, column= 1, columnspan=2)

insert_text2 = '''"Complementary DNA is often used in gene cloning or as gene probes or in the creation of a cDNA library. When
scientists transfer a gene from one cell into another cell in order to express the new genetic material as a
protein in the recipient cell, the cDNA will be added to the recipient (rather than the entire gene), because the 
DNA for an entire gene may include DNA that does not code for the protein or that interrupts the coding 
sequence of the protein (e.g., introns). Partial sequences of cDNAs are often obtained as expressed sequence 
tags."'''
complementary_DNA_text.insert(END, insert_text2)

complementarity_label = Label(root, text='Complementarity: ')
complementarity_label.configure(bg='#bcb8ce')
complementarity_label.grid(padx=10, row=6, column=0, sticky=E)
complementarity_dna_label = Label(root, text='Complementary DNA: ')
complementarity_dna_label.configure(bg='#bcb8ce')
complementarity_dna_label.grid(pady=10, padx=10, row=7, column=0, sticky=E)

root.mainloop()