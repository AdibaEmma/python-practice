from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    file = open("data.txt", "a")
    file.write(f"{website_entry.get()} ")
    file.write("| ")
    file.write(f"{username_entry.get()} ")
    file.write("| ")
    file.write(f"{password_entry.get()}\n")
    file.close()
    clear_data()


def clear_data():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    username_entry.insert(0, "eabaagah@gmail.com")
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, columnspan=2, row=2)
username_entry.insert(0, "eabaagah@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
