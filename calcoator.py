import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        button_texts = [
            '7', '8', '9', '÷',
            '4', '5', '6', '×',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for text in button_texts:
            button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_button = tk.Button(root, text='C', font=("Arial", 18), command=self.clear_display)
        clear_button.grid(row=row, column=0, sticky="nsew")
        backspace_button = tk.Button(root, text='⌫', font=("Arial", 18), command=self.backspace)
        backspace_button.grid(row=row, column=1, sticky="nsew")

        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        self.root.bind('<Key>', self.on_key_press)

    def on_button_click(self, char):
        current_text = self.display.get()

        if char == '=':
            try:
                expression = current_text.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == '.':
            
            if '.' not in current_text.split()[-1]:
                self.display.insert(tk.END, char)
        else:
            self.display.insert(tk.END, char)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def backspace(self):
        current_text = self.display.get()
        self.display.delete(len(current_text) - 1, tk.END)

    def on_key_press(self, event):
        key = event.char
        if key.isnumeric() or key in '+-*/.':
            if key == '*':
                key = '×'
            elif key == '/':
                key = '÷'
            self.on_button_click(key)
        elif key == '\r':
            self.on_button_click('=')
        elif key == '\b':
            self.backspace()
        elif key.lower() == 'c':
            self.clear_display()

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
