import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Label for password length input
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)

        # Entry for password length input
        self.length_entry = tk.Entry(root, width=20)
        self.length_entry.pack(pady=5)

        # Button to generate password
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg='light green')
        self.generate_button.pack(pady=5)

        # Label to display the generated password
        self.password_label = tk.Label(root, text="", font=('Arial', 12))
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer")
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        self.password_label.config(text=password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
