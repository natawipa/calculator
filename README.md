# Calculator Application

This is a simple calculator application implemented in Python using the Tkinter library for the graphical user interface. The calculator supports basic arithmetic operations, including addition, subtraction, multiplication, and division, as well as some mathematical functions like square root, exponential, and logarithm.

## How to Run

To run the calculator application, execute the `main.py` file. This will launch the graphical user interface where you can perform calculations.

```bash
python main.py
```

## Features

- Normal operations: Addition, subtraction, multiplication, and division.
- Mathematical functions: Square root, exponential, and logarithm.
- History display: Keeps track of previous calculations.


## Implementation Details

The application follows the Model-View-Controller (MVC) design pattern:
- Model: The Model class represents the data and business logic of the application. It stores the calculation history.
- View: The UI components (CalculatorUI and Keypad) present the user interface elements and capture user input.
- Controller: The CalculatorUI class contains event handlers and logic to interpret user actions and update the Model or View accordingly.