# color palette = https://paletasdecolores.com/paleta-de-colores-4264/
from os import error
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pyperclip
import re

root = Tk()
root.configure(bg="#bcb8ce")
root.title("DNA sequence generator")
root.iconbitmap("d:/Cosas de más/Programación/Repos/dna sequence generator/adn.ico")
root.geometry("960x465")


def error_messages(type_message):
    if type_message == "Wrong input":
        pop_up = messagebox.showerror(
            "Wrong input",
            "You should ONLY submit a sequence that is composed by the nitrogen-containing nucleobases (cytosine [C], guanine [G], adenine [A] or thymine [T])",
        )
    elif type_message == "Copy to clipboard":
        pop_up = messagebox.showerror(
            "Copy to clipboard error", "No text to copy into the clipboard"
        )
    elif type_message == "Export to file":
        pop_up = messagebox.showerror(
            "Export to file error", "No text to export into the file"
        )


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


def generate_sequences(dictionary, mode):
    global export_text
    global input_sequence
    global complementary_sequence
    global reverse_sequence
    global reverse_complementary_sequence
    export_text = []
    input_sequence = input_entry.get().upper()
    export_text.append(f"Input {mode} sequence: {input_sequence}\n")
    if re.match(r"[CGTAU]+$", input_sequence) is None:
        error_messages(type_message="Wrong input")
    else:
        complementary_sequence = "".join(
            [dictionary[nucleobase] for nucleobase in input_sequence]
        )
        export_text.append(f"Complementary {mode} sequence: {complementary_sequence}\n")
        reverse_sequence = input_sequence[::-1]
        export_text.append(f"Reverse {mode} sequence: {reverse_sequence}\n")
        reverse_complementary_sequence = complementary_sequence[::-1]
        export_text.append(
            f"Reverse complementary {mode} sequence: {reverse_complementary_sequence}\n"
        )
        display_entries(
            input_sequence,
            complementary_sequence,
            reverse_sequence,
            reverse_complementary_sequence,
        )


def copy_clipboard(sequence):
    if sequence == "input sequence":
        if not input_entry.get():
            error_messages(type_message="Copy to clipboard")
        else:
            pyperclip.copy(input_sequence)
    elif sequence == "complementary sequence":
        if not complementary_entry.get():
            error_messages(type_message="Copy to clipboard")
        else:
            pyperclip.copy(complementary_sequence)
    elif sequence == "reverse sequence":
        if not reverse_entry.get():
            error_messages(type_message="Copy to clipboard")
        else:
            pyperclip.copy(reverse_sequence)
    elif sequence == "reverse complementary sequence":
        if not reverse_complementary_entry.get():
            error_messages(type_message="Copy to clipboard")
        else:
            pyperclip.copy(reverse_complementary_sequence)


def export_file(action):
    if (
        not input_entry.get
        or not complementary_entry.get()
        or not reverse_entry.get()
        or not reverse_complementary_entry.get()
    ):
        error_messages(type_message="Export to file")
    else:
        if action == "New":
            file = filedialog.asksaveasfile(
                mode="w",
                title="Save file as",
                filetypes=(("Plain Text", "*.txt"), ("Markdown", "*.md")),
                initialdir="d:/Cosas de más/Programación/Repos/dna sequence generator",
            )
            for line in export_text:
                file.write(line)
            file.close()
        elif action == "Existing":
            file = filedialog.askopenfilename(
                title="Open a file",
                filetypes=(("Plain Text", "*.txt"), ("Markdown", "*.md")),
                initialdir="d:/Cosas de más/Programación/Repos/dna sequence generator",
            )
            for line in export_text:
                file.write(line)
        file.close()


# Input sequence
input_label = Label(root, text="Input sequence: ", bg="#bcb8ce")
input_label.grid(pady=10, padx=10, row=0, column=0, sticky=E)
input_entry = Entry(
    root,
    borderwidth=5,
    width=100,
)
input_entry.grid(pady=10, padx=10, row=0, column=1, columnspan=2)
input_copy_button = Button(
    root, text="Copy to clipboard", command=lambda: copy_clipboard("input sequence")
)
input_copy_button.grid(row=0, column=4)
# complementary sequence
complementary_label = Label(root, text="Complementary sequence: ", bg="#bcb8ce")
complementary_label.grid(pady=10, padx=10, row=1, column=0, sticky=E)
complementary_entry = Entry(root, borderwidth=5, width=100, state=DISABLED)
complementary_entry.grid(pady=10, padx=10, row=1, column=1, columnspan=2)
complementary_copy_button = Button(
    root,
    text="Copy to clipboard",
    command=lambda: copy_clipboard("complementary sequence"),
)
complementary_copy_button.grid(row=1, column=4)
# reverse sequence
reverse_label = Label(root, text="Reverse sequence: ", bg="#bcb8ce")
reverse_label.grid(pady=10, padx=10, row=2, column=0, sticky=E)
reverse_entry = Entry(root, borderwidth=5, width=100, state=DISABLED)
reverse_entry.grid(pady=10, padx=10, row=2, column=1, columnspan=2)
reverse_copy_button = Button(
    root, text="Copy to clipboard", command=lambda: copy_clipboard("reverse sequence")
)
reverse_copy_button.grid(row=2, column=4)
# reverse complementary sequence
reverse_complementary_label = Label(
    root, text="Reverse complementary sequence: ", bg="#bcb8ce"
)
reverse_complementary_label.grid(pady=10, padx=10, row=3, column=0, sticky=E)
reverse_complementary_entry = Entry(root, borderwidth=5, width=100, state=DISABLED)
reverse_complementary_entry.grid(pady=10, padx=10, row=3, column=1, columnspan=2)
reverse_complementary_copy_button = Button(
    root,
    text="Copy to clipboard",
    command=lambda: copy_clipboard("reverse complementary sequence"),
)
reverse_complementary_copy_button.grid(row=3, column=4)

# Mode
action = StringVar()

rna_action = Radiobutton(
    root,
    text="RNA",
    variable=action,
    value="RNA",
    bg="#bcb8ce",
    command=lambda: generate_sequences(
        dictionary={"A": "U", "T": "A", "C": "G", "G": "C"}, mode="RNA"
    ),
)
dna_action = Radiobutton(
    root,
    text="DNA",
    variable=action,
    value="DNA",
    bg="#bcb8ce",
    command=lambda: generate_sequences(
        dictionary={"A": "T", "T": "A", "C": "G", "G": "C"}, mode="ADN"
    ),
)
action.set("DNA")

rna_action.grid(row=5, column=1)
dna_action.grid(row=5, column=2)

mode_label = Label(root, text="Mode: ", bg="#bcb8ce")
mode_label.grid(pady=10, padx=10, row=5, column=0, sticky=E)

# Export to buttons
save_to_label = Label(root, text="Save sequences to: ", bg="#bcb8ce")
save_to_label.grid(pady=10, padx=10, row=6, column=0, sticky=E)
save_file_button = Button(
    root, text="New file", width=20, command=lambda: export_file(action="New")
)

save_file_button.grid(row=6, column=1, pady=10)
open_file_button = Button(
    root, text="Existing file", width=20, command=lambda: export_file(action="Existing")
)

open_file_button.grid(row=6, column=2, pady=10)

# Texts
complementary_text = Text(
    root, height=5, width=87, bg="#bcb8ce", font=("Calibri", 10), bd=0
)
complementary_text.grid(row=7, column=1, columnspan=2)

insert_text1 = '''"In molecular biology, complementarity is a property shared between two nucleic acid sequences, such that
when they are aligned antiparallel to each other, the nucleotide bases at each position will be complementary.
Two bases are complementary if they form Watson-Crick base pairs. The degree of complementarity between
two nucleic acid strands may vary, from total complementarity to none. This tools calculates total 
complementary sequence."'''
complementary_text.insert(END, insert_text1)

complementary_DNA_text = Text(
    root, height=6, width=87, bg="#bcb8ce", font=("Calibri", 10), bd=0, pady=10
)
complementary_DNA_text.grid(row=8, column=1, columnspan=2)

insert_text2 = '''"Complementary DNA is often used in gene cloning or as gene probes or in the creation of a cDNA library. When
scientists transfer a gene from one cell into another cell in order to express the new genetic material as a
protein in the recipient cell, the cDNA will be added to the recipient (rather than the entire gene), because the 
DNA for an entire gene may include DNA that does not code for the protein or that interrupts the coding 
sequence of the protein (e.g., introns). Partial sequences of cDNAs are often obtained as expressed sequence 
tags."'''
complementary_DNA_text.insert(END, insert_text2)

complementarity_label = Label(root, text="Complementarity: ", bg="#bcb8ce")
complementarity_label.grid(padx=10, row=7, column=0, sticky=E)
complementarity_dna_label = Label(root, text="Complementary DNA: ", bg="#bcb8ce")
complementarity_dna_label.grid(pady=10, padx=10, row=8, column=0, sticky=E)


root.mainloop()
