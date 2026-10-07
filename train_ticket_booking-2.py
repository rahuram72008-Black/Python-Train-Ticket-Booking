import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect("train.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS booking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    passenger_name TEXT NOT NULL,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    journey_date TEXT NOT NULL,
    train TEXT NOT NULL
)
""")
conn.commit()

stations = ["Dindigul", "Trichy", "Madurai", "Chennai", "Coimbatore"]
trains = ["Intercity Express", "Vaigai Express", "Pandian Express", "Rockfort Express"]

def book_ticket():
    name = name_entry.get().strip()
    source = source_box.get()
    destination = destination_box.get()
    date = date_entry.get().strip()
    train = train_box.get()

    if not name or not date or not source or not destination or not train:
        messagebox.showwarning("Missing", "Please fill all details.")
        return

    if source == destination:
        messagebox.showerror("Error", "From and To cannot be the same.")
        return

    cur.execute(
        "INSERT INTO booking(passenger_name, source, destination, journey_date, train) VALUES (?, ?, ?, ?, ?)",
        (name, source, destination, date, train)
    )
    conn.commit()

    messagebox.showinfo(
        "Booking Confirmed",
        f"Passenger: {name}\nFrom: {source}\nTo: {destination}\n"
        f"Date: {date}\nTrain: {train}"
    )

root = tk.Tk()
root.title("Train Ticket Booking")
root.geometry("400x430")

tk.Label(root, text="TRAIN TICKET BOOKING", font=("Arial", 18, "bold")).pack(pady=15)

tk.Label(root, text="Passenger Name").pack()
name_entry = tk.Entry(root, width=35)
name_entry.pack(pady=5)

tk.Label(root, text="From").pack()
source_box = ttk.Combobox(root, values=stations, state="readonly", width=32)
source_box.pack(pady=5)

tk.Label(root, text="To").pack()
destination_box = ttk.Combobox(root, values=stations, state="readonly", width=32)
destination_box.pack(pady=5)

tk.Label(root, text="Journey Date").pack()
date_entry = tk.Entry(root, width=35)
date_entry.insert(0, "20-08-2026")
date_entry.pack(pady=5)

tk.Label(root, text="Train").pack()
train_box = ttk.Combobox(root, values=trains, state="readonly", width=32)
train_box.pack(pady=5)

tk.Button(root, text="BOOK TICKET", command=book_ticket, width=20).pack(pady=20)

root.mainloop()
conn.close()
