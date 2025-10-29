import tkinter as tk
from tkinter import messagebox
from business_layer import BusinessLayer

# Database connection string
CONN = "dbname=postgres user=L015811 password= host=localhost port=5432"

# Create business layer instance
bl = BusinessLayer(CONN)

# Initialize GUI
root = tk.Tk()
root.title("IN450 Unit 2 Data Access Application")
root.geometry("520x420")

# Header
header = tk.Label(
    root, 
    text="IN450 Unit 2 — Data Access (PostgreSQL + Tkinter)", 
    font=("Arial", 12, "bold")
)
header.pack(pady=8)

# Output text area
output = tk.Text(root, height=16, width=62)
output.pack(padx=10, pady=8)

def show_row_count():
    """Display row count from in450a table."""
    output.delete("1.0", tk.END)
    try:
        count = bl.get_row_count_in450a()
        output.insert(tk.END, f"Rows in in450a: {count}\n")
    except Exception as ex:
        messagebox.showerror("Error", f"Failed to get row count.\n{ex}")

def show_names():
    """Display first and last names from in450b table."""
    output.delete("1.0", tk.END)
    try:
        names = bl.get_names_in450b()
        if not names:
            output.insert(tk.END, "No names found in in450b.\n")
        else:
            for first, last in names:
                output.insert(tk.END, f"{first} {last}\n")
    except Exception as ex:
        messagebox.showerror("Error", f"Failed to get names.\n{ex}")

# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=6)

tk.Button(
    btn_frame, 
    text="Get Row Count (in450a)", 
    command=show_row_count
).grid(row=0, column=0, padx=6, pady=4)

tk.Button(
    btn_frame, 
    text="Show Names (in450b)", 
    command=show_names
).grid(row=0, column=1, padx=6, pady=4)

tk.Button(
    btn_frame, 
    text="Close", 
    command=root.destroy
).grid(row=0, column=2, padx=6, pady=4)

if __name__ == "__main__":
    root.mainloop()