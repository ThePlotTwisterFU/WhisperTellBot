import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Funktion zum Anzeigen der persönlichen Details
def show_details():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    birthdate = birthdate_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()

    details_text = f"Name: {name}\n" \
                   f"Alter: {age}\n" \
                   f"E-Mail: {email}\n" \
                   f"Geburtsdatum: {birthdate}\n" \
                   f"Adresse: {address}\n" \
                   f"Telefonnummer: {phone}"

    messagebox.showinfo("Persönliche Details", details_text)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Persönliche Details")
root.geometry("400x300")

# Hintergrundfarbe
root.configure(bg="#f0f0f0")

# Rahmen für persönliche Details
frame_style = ttk.Style()
frame_style.configure("My.TFrame", background="#d3d3d3")
info_frame = ttk.Frame(root, style="My.TFrame", padding=(10, 10, 10, 0))
info_frame.pack(fill="both", expand=True)

# Eingabefelder für persönliche Details
font_style = ("Arial", 12)

tk.Label(info_frame, text="Name:", bg="#d3d3d3", font=font_style).grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(info_frame, font=font_style)
name_entry.grid(row=0, column=1)

tk.Label(info_frame, text="Alter:", bg="#d3d3d3", font=font_style).grid(row=1, column=0, sticky="w")
age_entry = tk.Entry(info_frame, font=font_style)
age_entry.grid(row=1, column=1)

tk.Label(info_frame, text="E-Mail:", bg="#d3d3d3", font=font_style).grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(info_frame, font=font_style)
email_entry.grid(row=2, column=1)

tk.Label(info_frame, text="Geburtsdatum:", bg="#d3d3d3", font=font_style).grid(row=3, column=0, sticky="w")
birthdate_entry = tk.Entry(info_frame, font=font_style)
birthdate_entry.grid(row=3, column=1)

tk.Label(info_frame, text="Adresse:", bg="#d3d3d3", font=font_style).grid(row=4, column=0, sticky="w")
address_entry = tk.Entry(info_frame, font=font_style)
address_entry.grid(row=4, column=1)

tk.Label(info_frame, text="Telefonnummer:", bg="#d3d3d3", font=font_style).grid(row=5, column=0, sticky="w")
phone_entry = tk.Entry(info_frame, font=font_style)
phone_entry.grid(row=5, column=1)

# Button zum Anzeigen der persönlichen Details
show_button = tk.Button(root, text="Details anzeigen", command=show_details, bg="#4CAF50", fg="white", font=font_style)
show_button.pack(pady=10)

# Hover-Effekt für den Button
def on_enter(e):
    show_button['background'] = '#45a049'
def on_leave(e):
    show_button['background'] = '#4CAF50'
show_button.bind("<Enter>", on_enter)
show_button.bind("<Leave>", on_leave)

# Starte die GUI-Schleife
root.mainloop()
