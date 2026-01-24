"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().
"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
firstNumber = simpledialog.askinteger('1st Number',"Enter a number")
# Ask the user for the second number
secondNumber = simpledialog.askinteger('2nd Number',"Enter another number")
# Ask the user for the math operation
operation = simpledialog.askstring('Operation',"What math operation do you want to use?")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if operation == "add":
   messagebox.showinfo('Sum:',firstNumber+secondNumber)
elif operation == "subtract":
   messagebox.showinfo('Difference:',firstNumber-secondNumber)
elif operation == "multiply":
   messagebox.showinfo('Product:',firstNumber * secondNumber)
elif operation == "divide":
   messagebox.showinfo('Quotient:',firstNumber/secondNumber)
else:
   messagebox.showerror('ERROR!',"You entered an unknown operation, please restart and try again.")
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
window.mainloop()