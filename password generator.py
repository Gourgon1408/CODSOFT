import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Create and place the widgets
        tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.uppercase_var = tk.BooleanVar()
        self.lowercase_var = tk.BooleanVar()
        self.digits_var = tk.BooleanVar()
        self.special_var = tk.BooleanVar()

        tk.Checkbutton(root, text="Include Uppercase", variable=self.uppercase_var).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Checkbutton(root, text="Include Lowercase", variable=self.lowercase_var).grid(row=1, column=1, padx=10, pady=5, sticky="w")
        tk.Checkbutton(root, text="Include Digits", variable=self.digits_var).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Checkbutton(root, text="Include Special Characters", variable=self.special_var).grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.password_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = self.length_entry.get()

        if not length.isdigit() or int(length) <= 0:
            messagebox.showerror("Input Error", "Please enter a valid number for password length.")
            return

        length = int(length)
        characters = ""

        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Selection Error", "Please select at least one character set.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(tk.END, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
