import tkinter as tk
from tkinter import messagebox
import tkinter.font as font


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x500")
        self.root.configure(bg="#F0F0F0")
        self.current_theme = "light"

        self.create_widgets()
        self.update_button_styles()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, justify="right", font=(
            "Arial", 20), bg="#F0F0F0", fg="#333333")
        self.entry.grid(row=0, column=0, columnspan=4,
                        padx=10, pady=10, sticky="nsew")

        self.history = tk.Listbox(self.root, bg="#F0F0F0", fg="#333333", font=(
            "Arial", 10), width=30, height=8)
        self.history.grid(row=1, column=0, columnspan=4,
                          padx=10, pady=5, sticky="nsew")

        self.button_frame = tk.Frame(self.root, bg="#F0F0F0")
        self.button_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        button_labels = {
            "7": (0, 0), "8": (0, 1), "9": (0, 2), "/": (0, 3),
            "4": (1, 0), "5": (1, 1), "6": (1, 2), "*": (1, 3),
            "1": (2, 0), "2": (2, 1), "3": (2, 2), "-": (2, 3),
            "0": (3, 0), ".": (3, 1), "=": (3, 2), "+": (3, 3),
        }

        self.buttons = {}
        for label, (row, column) in button_labels.items():
            btn = tk.Button(self.button_frame, text=label, font=("Arial", 15), padx=20, pady=10, bd=0,
                            command=lambda value=label: self.add_to_expression(value))
            btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
            self.buttons[label] = btn

        self.buttons["="].config(command=self.calculate)

        self.theme_button = tk.Button(self.root, text="\u2600", font=font.Font(family='Arial', size=12),
                                      command=self.toggle_theme)
        self.theme_button.grid(row=3, column=0, columnspan=4,
                               padx=10, pady=10, sticky="nsew")

        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            self.history.insert(tk.END, f"{expression} = {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")

    def update_button_styles(self):
        bg_color = "#F0F0F0" if self.current_theme == "light" else "#2C3E50"
        fg_color = "#333333" if self.current_theme == "light" else "#ECF0F1"

        for btn in self.buttons.values():
            btn.config(bg=bg_color, fg=fg_color, relief=tk.FLAT, bd=2)

    def toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"

        bg_color = "#F0F0F0" if self.current_theme == "light" else "#2C3E50"
        fg_color = "#333333" if self.current_theme == "light" else "#ECF0F1"

        self.root.config(bg=bg_color)
        self.entry.config(bg=bg_color, fg=fg_color)
        self.history.config(bg=bg_color, fg=fg_color)
        self.button_frame.config(bg=bg_color)

        if self.current_theme == "light":
            self.theme_button.config(text="\u2600", bg="#F0F0F0", fg="#333333")
        else:
            self.theme_button.config(text="\u263E", bg="#2C3E50", fg="#ECF0F1")

        self.update_button_styles()

    def add_to_expression(self, value):
        self.entry.insert(tk.END, value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
