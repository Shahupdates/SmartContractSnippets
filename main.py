import tkinter as tk
from tkinter import filedialog, Text

# Initialise Tkinter
root = tk.Tk()
root.title("Smart Contract Builder")
root.geometry("800x600")

# Create frames for file selection and text editor
frame1 = tk.Frame(root, bg="#263D42")
frame1.place(relwidth=0.3, relheight=1)

frame2 = tk.Frame(root, bg="#263D42")
frame2.place(relx=0.3, relwidth=0.7, relheight=1)

# Create Listbox for file selection
listbox = tk.Listbox(frame1, font=("Helvetica", 16))
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add file names to the Listbox
listbox.insert(tk.END, "Ethereum/ERC20.sol")
listbox.insert(tk.END, "Ethereum/ERC721.sol")
listbox.insert(tk.END, "BinanceSmartChain/BEP20.sol")
listbox.insert(tk.END, "BinanceSmartChain/BEP721.sol")
listbox.insert(tk.END, "Solana/helloworld/lib.rs")
listbox.insert(tk.END, "Polkadot/flipper/lib.rs")

# Create Text widget for text editor
text = tk.Text(frame2, font=("Helvetica", 16))
text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Function to open the selected file and insert its content at the cursor position
def insert_file():
    # Get selected file
    file = listbox.get(listbox.curselection())

    # Read the file
    with open(file, "r") as f:
        content = f.read()

    # Insert content at cursor position
    text.insert(tk.INSERT, content)

# Create button to insert the selected file
button = tk.Button(frame1, text="Insert snippet", command=insert_file)
button.pack(side=tk.BOTTOM, padx=10, pady=10)

root.mainloop()
