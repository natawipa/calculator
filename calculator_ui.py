from tkinter import *
from tkinter import ttk
from model import Model
from keypad import Keypad
from math import sqrt, exp, log, log2, log10
import pygame

class CalculatorUI(Tk):
    def __init__(self):
        super().__init__()
        self.model = Model()
        self.init_components()
        self.current_expression = ""
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("click.wav")

    def init_components(self):
        self.title("Calculator")
        self.style = ttk.Style()
        self.style.configure("TButton", font=('Monaco', 16), background="gray", foreground="navy")
        self.display = Entry(self, justify="right", state="readonly")
        self.numpad = self.make_numpad()
        self.operatorpad = self.make_operatorpad()
        frame = Frame(self)
        self.functions = ttk.Combobox(frame, values=[
            "sqrt", "exp", "log", "log2", "log10"
        ], state="readonly", style="TButton")
        self.functions.set("sqrt")
        self.functions.bind("<<ComboboxSelected>>", self.on_function_selected)
        self.functions.pack(side=TOP, fill=BOTH, expand=True)
        self.history = Listbox(frame)
        self.update_history()
        self.history.pack(side=TOP, fill=BOTH, expand=True)

        self.display.pack(side=TOP, fill=BOTH, expand=True)
        self.numpad.pack(side=LEFT, fill=BOTH, expand=True)
        self.operatorpad.pack(side=LEFT, fill=BOTH, expand=True)
        frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def make_numpad(self):
        numpad = Keypad(self, keynames=[
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            ".", "0", "="
        ], columns=3)
        numpad.bind("<Button-1>", self.on_click)
        return numpad

    def make_operatorpad(self):
        operatorpad = Keypad(self, keynames=[
            "+", "-", "*", "/",
            "(", ")", "CLR", "DEL"
        ], columns=2)
        operatorpad.bind("<Button-1>", self.on_click)

        return operatorpad
    
    def run(self):
        self.mainloop()

    # Controller
    def on_click(self, event):
        clicked_button = event.widget
        text = clicked_button["text"]
        
        if text == "=":
            result = self.calculate(self.current_expression)
            self.display.config(state="normal")
            self.display.delete(0, END)
            self.display.insert(END, str(result))
            self.display.config(state="readonly")
            self.current_expression = ""
            self.update_history()
        elif text == "CLR":
            self.display.config(state="normal")
            self.display.delete(0, END)
            self.display.config(state="readonly")
            self.current_expression = ""
        elif text == "DEL":
            self.current_expression = self.current_expression[:-1]
            self.display.config(state="normal")
            self.display.delete(len(self.current_expression), END)
            self.display.config(state="readonly")
        else:
            self.current_expression += text
            self.display.config(state="normal")
            self.display.insert(END, text)
            self.display.config(state="readonly")
            self.play_click_sound()

    def on_function_selected(self, event):
        function = self.functions.get()
        self.current_expression += function + "("
        self.display.config(state="normal")
        self.display.insert(END, f"{function}(")
        self.display.config(state="readonly")

    def play_click_sound(self):
        self.click_sound.play()

    def calculate(self, expression):
        try:
            result = eval(expression)
            self.model.add_to_history(f"{expression} = {result}")
            return f"{result:.2f}"
        except Exception as e:
            return f"Error: {e}"
        
    def update_history(self):
        self.history.delete(0, END)
        for item in self.model.get_history():
            self.history.insert(END, item)