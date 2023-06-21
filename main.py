import tkinter as tk
from tkinter import filedialog, Text, scrolledtext, messagebox
from tkinter import ttk
import os

# Initialise Tkinter
root = tk.Tk()
root.title("Smart Contract Builder")
root.geometry("800x600")

# Change the theme of the application
style = ttk.Style(root)
style.theme_use("clam")  # Change according to your preference

# Function to get files from the directory
def get_files(dir_path):
    files = []
    for root, dirs, filenames in os.walk(dir_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

# Create Listbox for file selection
listbox = tk.Listbox(root, font=("Consolas", 12))
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add file names to the Listbox
for file in get_files("SmartContractSnippets"):
    listbox.insert(tk.END, file)

# Create Text widget for text editor
text = scrolledtext.ScrolledText(root, undo=True, font=("Consolas", 12))
text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Function to open the selected file and insert its content at the cursor position
def insert_file(event=None):
    # Get selected file
    file = listbox.get(listbox.curselection())

    # Read the file
    try:
        with open(file, "r") as f:
            content = f.read()

        # Insert content at cursor position
        text.insert(tk.INSERT, content)
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")

# Bind double click event to listbox
listbox.bind("<Double-Button-1>", insert_file)

root.mainloop()
