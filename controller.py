from tkinter import *
from model import Model
from calculator_ui import CalculatorUI


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = CalculatorUI()
        self.current_expression = ""
        
        self.view.numpad.bind("<Button-1>", self.on_click)
        self.view.operatorpad.bind("<Button-1>", self.on_click)
        self.view.functions.bind("<<ComboboxSelected>>", self.on_function_selected)
        
    def on_click(self, event):
        clicked_button = event.widget
        text = clicked_button["text"]
        
        if text == "=":
            result = self.calculate(self.current_expression)
            self.view.display.config(state="normal")
            self.view.display.delete(0, END)
            self.view.display.insert(END, str(result))
            self.view.display.config(state="readonly")
            self.current_expression = ""
            self.update_history()
        elif text == "CLR":
            self.view.display.config(state="normal")
            self.view.display.delete(0, END)
            self.view.display.config(state="readonly")
            self.current_expression = ""
        elif text == "DEL":
            self.current_expression = self.current_expression[:-1]
            self.view.display.config(state="normal")
            self.view.display.delete(len(self.current_expression), END)
            self.view.display.config(state="readonly")
        else:
            self.current_expression += text
            self.view.display.config(state="normal")
            self.view.display.insert(END, text)
            self.view.display.config(state="readonly")
            
    def on_function_selected(self, event):
        function = self.view.functions.get()
        self.current_expression += function + "("
        self.view.display.config(state="normal")
        self.view.display.insert(END, f"{function}(")
        self.view.display.config(state="readonly")
        
    def calculate(self, expression):
        try:
            result = eval(expression)
            self.model.add_to_history(f"{expression} = {result}")
            return f"{result:.2f}"
        except Exception as e:
            return f"Error: {e}"
        
    def update_history(self):
        self.view.history.delete(0, END)
        for item in self.model.get_history():
            self.view.history.insert(END, item)