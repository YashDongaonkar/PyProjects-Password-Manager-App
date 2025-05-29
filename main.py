import tkinter as tk
from tkinter import ttk
from random import choice, randint, shuffle

import json

from tkinter import messagebox

# ----------------- PASSWORD GENERATOR -------------------------------------

def gen_pswd():        
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    pswd = "".join(password_list)

    password.delete(0,tk.END)
    password.insert(0,pswd)

    window.clipboard_clear()
    window.clipboard_append(pswd)


def grid_place(item,row,column,columnspan=1):
    item.grid(row = row,column = column,columnspan = columnspan)

# ---------------- SAVE DATA -----------------------------------------------
def store():

    website = website_input.get().title()
    eu = EU_input.get()
    pswd = password.get()

    if len(website) == 0:
        messagebox.showerror(title="Error",message="Empty website field")
        return

    if len(pswd) == 0:
        messagebox.showerror(title="Error",message="Empty password field")
        return

    is_ok = messagebox.askokcancel(title="Confirmation",
                           message=f"Details:\nWebsite: {website}\nEmail/Username: {eu}\nPassword: {pswd}\nProceed ?")

    if is_ok:
        new_data = {
            website:{
                "eu":eu,
                "pswd":pswd
            }
        }
        try:
            with open("data.json","r") as f:
                # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json","w") as f:
                json.dump(new_data,f,indent = 4)
        else:
            # Updating old data
            data.update(new_data)

            with open("data.json","w") as f:
                # Saving updated data
                json.dump(new_data,f,indent=4)
        finally:
            website_input.delete(0,tk.END)
            password.delete(0,tk.END)

    
def search():

    website = website_input.get().title()

    try:
        with open("data.json") as f:
            data = json.load(f)
            messagebox.showinfo(title="Search Result",message=f"For {website}\nPasword is{data[website]["pswd"]}")
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No passwords stored yet")
    except KeyError:
        messagebox.showerror(title="Error",message=f"Password does not exist for {website}\nCheck for typos or create a new password")

window = tk.Tk()
window.title("Password Manager")
window.config(padx = 40,pady = 40)

# Components

website_label = ttk.Label(text="Website:")
website_input = ttk.Entry(width = 22)
search_btn = ttk.Button(text = "Search", command = search)

EU_label = ttk.Label(text="Email/Username:")
EU_input = ttk.Entry(width = 35)

password_label = ttk.Label(text="Password:")
password = ttk.Entry(width = 22)
generate_btn = ttk.Button(text="Generate",command = gen_pswd)

add_btn = ttk.Button(text = "Add",width = 34, command = store)

# Layout
grid_place(website_label, 0, 0)
grid_place(website_input, 0, 1)
grid_place(search_btn,0,2)

grid_place(EU_label, 1, 0)
grid_place(EU_input, 1, 1, 2)

grid_place(password_label, 2, 0)
grid_place(password, 2, 1)
grid_place(generate_btn, 2,2)

grid_place(add_btn, 3, 1,3)

website_input.focus()
EU_input.insert(0,"yashdongaonkar94@gmail.com")

window.mainloop()