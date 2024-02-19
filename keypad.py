from tkinter import *
from tkinter import ttk

class Keypad(Frame):
    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns):
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        self.style = ttk.Style()
        self.style.configure("TButton", font=('Monaco', 16), background="gray", foreground="navy")
        row = 0
        col = 0
        for keyname in self.keynames:
            button = ttk.Button(self, text=keyname, style="TButton")
            button.grid(row=row, column=col, sticky=NSEW, padx=2, pady=2)
            col += 1
            if col >= columns:
                col = 0
                row += 1
        for i in range(columns):
            self.columnconfigure(i, weight=1)
        for i in range(row):
            self.rowconfigure(i, weight=1)


    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        for child in self.winfo_children():
            child.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.
        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for child in self.winfo_children():
            child[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.winfo_children()[0][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.
        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for child in self.winfo_children():
            child.configure(cnf, **kwargs)

    @property
    def frame(self):
        return self