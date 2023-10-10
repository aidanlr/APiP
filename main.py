import tkinter as tk
import customtkinter

def clear_entries():
    ent_force.delete(0, tk.END)
    ent_mass.delete(0, tk.END)
    ent_accel.delete(0, tk.END)

def calculate():
    force = ent_force.get().strip()
    mass = ent_mass.get().strip()
    accel = ent_accel.get().strip()
    
    error_label.pack_forget()  # Clear any existing error message
    
    if force == "" and mass == "" and accel == "":
        error_label.pack()
        clear_entries()
    elif force == "":
        # Calculate force if it's missing
        mass = float(mass)
        accel = float(accel)
        result = mass * accel
        ent_force.delete(0, tk.END)  # Clear any existing text in the Entry
        ent_force.insert(0, str(result))  # Insert the result into the Entry as a string
    elif mass == "":
        # Calculate mass if it's missing
        force = float(force)
        accel = float(accel)
        result = force / accel
        ent_mass.delete(0, tk.END)  # Clear any existing text in the Entry
        ent_mass.insert(0, str(result))  # Insert the result into the Entry as a string
    elif accel == "":
        # Calculate acceleration if it's missing
        force = float(force)
        mass = float(mass)
        result = force / mass
        ent_accel.delete(0, tk.END)  # Clear any existing text in the Entry
        ent_accel.insert(0, str(result))  # Insert the result into the Entry as a string
    else:
        error_label.pack()
        clear_entries()

window = customtkinter.CTk()
window.title("Newton's First Law Calculator")

frame_nav = customtkinter.CTkFrame(master=window, border_color="#ffffff")
frame_calc = customtkinter.CTkFrame(master=window, border_color="#ffffff")

title = customtkinter.CTkLabel(master=frame_nav, text="Newton's First Law Calculator")
title.pack()

lbl_force = customtkinter.CTkLabel(master=frame_calc, text="Force (N)")
lbl_force.pack()
ent_force = customtkinter.CTkEntry(master=frame_calc)
ent_force.pack()

lbl_mass = customtkinter.CTkLabel(master=frame_calc, text="Mass (kg)")
lbl_mass.pack()
ent_mass = customtkinter.CTkEntry(master=frame_calc)
ent_mass.pack()

lbl_accel = customtkinter.CTkLabel(master=frame_calc, text="Acceleration (m/s\u00b2)")
lbl_accel.pack()
ent_accel = customtkinter.CTkEntry(master=frame_calc)
ent_accel.pack()

error_label = customtkinter.CTkLabel(master=frame_calc, text="Please enter two out of three parameters.", text_color="red")

btn_submit = customtkinter.CTkButton(master=frame_calc, text="Calculate", command=calculate)
btn_submit.pack(pady=15)

frame_nav.pack(padx=10, pady=10)
frame_calc.pack(padx=10, pady=10)

window.mainloop()
