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
    gender = gender_var.get()
    profession = profession_entry.get()
    marital_status = marital_status_var.get()
    hobby = hobby_entry.get()
    music = music_entry.get()
    film = film_entry.get()
    book = book_entry.get()

    details_text = f"Name: {name}\n" \
                   f"Alter: {age}\n" \
                   f"E-Mail: {email}\n" \
                   f"Geburtsdatum: {birthdate}\n" \
                   f"Adresse: {address}\n" \
                   f"Telefonnummer: {phone}\n" \
                   f"Geschlecht: {gender}\n" \
                   f"Beruf: {profession}\n" \
                   f"Familienstand: {marital_status}\n" \
                   f"Lieblingshobby: {hobby}\n" \
                   f"Lieblingsmusik: {music}\n" \
                   f"Lieblingsfilm: {film}\n" \
                   f"Lieblingsbuch: {book}"

    messagebox.showinfo("Persönliche Details", details_text)

# Hauptfenster erstellen
root = tk.Tk()
root.title("WhisperTellBot (WTB)")
root.geometry("400x600")

# Hintergrundfarbe
root.configure(bg="#f0f0f0")

# Rahmen für persönliche Details
info_frame = ttk.Frame(root, style="My.TFrame", padding=20)
info_frame.pack(fill="both", expand=True)

# Stil für den Rahmen
style = ttk.Style()
style.configure("My.TFrame", background="#f0f0f0")

# Eingabefelder für persönliche Details
font_style = ("Arial", 12)

tk.Label(info_frame, text="Name:", font=font_style).grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(info_frame, font=font_style)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(info_frame, text="Alter:", font=font_style).grid(row=1, column=0, sticky="w", pady=5)
age_entry = tk.Entry(info_frame, font=font_style)
age_entry.grid(row=1, column=1, pady=5)

tk.Label(info_frame, text="E-Mail:", font=font_style).grid(row=2, column=0, sticky="w", pady=5)
email_entry = tk.Entry(info_frame, font=font_style)
email_entry.grid(row=2, column=1, pady=5)

tk.Label(info_frame, text="Geburtsdatum:", font=font_style).grid(row=3, column=0, sticky="w", pady=5)
birthdate_entry = tk.Entry(info_frame, font=font_style)
birthdate_entry.grid(row=3, column=1, pady=5)

tk.Label(info_frame, text="Adresse:", font=font_style).grid(row=4, column=0, sticky="w", pady=5)
address_entry = tk.Entry(info_frame, font=font_style)
address_entry.grid(row=4, column=1, pady=5)

tk.Label(info_frame, text="Telefonnummer:", font=font_style).grid(row=5, column=0, sticky="w", pady=5)
phone_entry = tk.Entry(info_frame, font=font_style)
phone_entry.grid(row=5, column=1, pady=5)

tk.Label(info_frame, text="Geschlecht:", font=font_style).grid(row=6, column=0, sticky="w", pady=5)
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(info_frame, textvariable=gender_var, values=["Männlich", "Weiblich", "Andere"], font=font_style)
gender_combobox.grid(row=6, column=1, pady=5)

tk.Label(info_frame, text="Beruf:", font=font_style).grid(row=7, column=0, sticky="w", pady=5)
profession_entry = tk.Entry(info_frame, font=font_style)
profession_entry.grid(row=7, column=1, pady=5)

tk.Label(info_frame, text="Familienstand:", font=font_style).grid(row=8, column=0, sticky="w", pady=5)
marital_status_var = tk.StringVar()
marital_status_combobox = ttk.Combobox(info_frame, textvariable=marital_status_var, values=["Ledig", "Verheiratet", "Geschieden", "Verwitwet"], font=font_style)
marital_status_combobox.grid(row=8, column=1, pady=5)

tk.Label(info_frame, text="Lieblingshobby:", font=font_style).grid(row=9, column=0, sticky="w", pady=5)
hobby_entry = tk.Entry(info_frame, font=font_style)
hobby_entry.grid(row=9, column=1, pady=5)

tk.Label(info_frame, text="Lieblingsmusik:", font=font_style).grid(row=10, column=0, sticky="w", pady=5)
music_entry = tk.Entry(info_frame, font=font_style)
music_entry.grid(row=10, column=1, pady=5)

tk.Label(info_frame, text="Lieblingsfilm:", font=font_style).grid(row=11, column=0, sticky="w", pady=5)
film_entry = tk.Entry(info_frame, font=font_style)
film_entry.grid(row=11, column=1, pady=5)

tk.Label(info_frame, text="Lieblingsbuch:", font=font_style).grid(row=12, column=0, sticky="w", pady=5)
book_entry = tk.Entry(info_frame, font=font_style)
book_entry.grid(row=12, column=1, pady=5)

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
creator_label = tk.Label(root, text="Created by ThePlotTwisterFU", bg="#f0f0f0", font=("Arial", 10)) creator_label.pack(side="bottom", pady=5)
root.mainloop()
