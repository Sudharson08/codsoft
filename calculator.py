import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""

        # Display screen
        self.display = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Number buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click(x)
            if button not in ['=', 'C']:
                tk.Button(root, text=button, width=5, height=2, command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
            else:
                if button == '=':
                    tk.Button(root, text=button, width=5, height=2, command=self.equal).grid(row=row_val, column=col_val, padx=5, pady=5)
                else:
                    tk.Button(root, text=button, width=5, height=2, command=self.clear).grid(row=row_val, column=col_val, padx=5, pady=5)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click(self, value):
        self.expression += value
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def equal(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
