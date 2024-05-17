import tkinter as tk

def process_input(event):
    # Get the text from the entry box
    input_text = value.get()
    
    # Print "hello world"
    print("hello world")
    
    # Clear the entry box
    entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Input Processor")

# Create the entry box
value = tk.StringVar()
entry = tk.Entry(root, textvariable=value)
entry.grid(row=0, column=0, padx=10, pady=10)
entry.focus()  # Set focus on the entry box initially

# Bind the Enter key (Return key) to the process_input function
entry.bind("<Return>", process_input)

# Run the Tkinter event loop
root.mainloop()
