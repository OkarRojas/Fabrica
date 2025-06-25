from tkinter import *
import os

root = Tk()
root.title("Login")
root.geometry("300x350")
root.resizable(False, False)

root.configure(bg="lightblue")

regis = Label(root, text="Register", font=("Arial", 20), bg="lightblue")
regis.pack(pady=20)

username_label = Label(root, text="Username", font=("Arial", 14), bg="lightblue")
username_label.pack(pady=5)

username_entry = Entry(root, font=("Arial", 14))
username_entry.pack(pady=5)

password_label = Label(root, text="Password", font=("Arial", 14), bg="lightblue")
password_label.pack(pady=5)

password_entry = Entry(root, show="*", font=("Arial", 14))
password_entry.pack(pady=5)

# Button to submit the form
submit_button = Button(root, text="Submit", font=("Arial", 14), command=lambda: submit())
submit_button.pack(pady=20)

def submit():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}, Password: {password}")
    
    root.destroy()

    os.system('python Main.py')
    


root.mainloop()

