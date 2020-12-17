import os
import tkinter as tk
from tkinter import *

#Functions to delete each individual screen
def delete3():
    screen3.destroy()


def delete4():
    screen4.destroy()


def delete5():
    screen5.destroy()

#Creation of the logic for theregister screen
def register_user():
    #Retrieves the username and password from the field boxes on the register screen
    username_info = username.get()
    password_info = password.get()

    #Writes the username and password to a file, that is named based on the username retrieved and stores the user's password and name into the file
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration successful", fg="green", bg="black").pack()

#Creation of the register screen, including the text, boxes, and submission button
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username").pack()
    username_entry = tk.Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password").pack()
    password_entry = tk.Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Finish Registration", width=20,
           height=2, command=register_user).pack()

#Creation of the login screen
def login():
    global screen2
    global username_verify
    global password_verify
    global username_entered
    global password_entered

    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Please enter Login details").pack()
    Label(screen2, text="").pack()
    Label(screen2, text="username").pack()
    username_entered = tk.Entry(screen2, textvariable=username_verify)
    username_entered.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password").pack()
    password_entered = tk.Entry(screen2, textvariable=password_verify)
    password_entered.pack()

    Button(screen2, text="Login", width=20,
           height=2, command=login_verify).pack()

#Logic for the login screen
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    #Clears the submission boxes once the user has entered submit
    username_entered.delete(0, END)
    password_entered.delete(0, END)

    #Loops over the list of files in the current directory
    list_of_files = os.listdir()
    #If the there is a file that is the same as the username, then open the file
    if username1 in list_of_files:
        file1 = open(username1, "r")
        #Stores the password into the variable verify
        verify = file1.read().splitlines()
        #If the verify is equal to the inputed password, than the user has successfully logined
        #Else the user has not logined
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()
    else:
        user_not_found()

#Destroys the login screen, and creates a screen that tells the user they have successfully logged in
def login_success():
    screen2.destroy()
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")

    Label(screen3, text="Login successful").pack()
    Button(screen3, text="Ok", command=delete3).pack()

#Creates an additional screen to tell the user they entered the wrong password, does not delete the login screen
def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Error")
    screen4.geometry("150x100")

    Label(screen4, text="Incorrect password").pack()
    Button(screen4, text="Ok", command=delete4).pack()

#Creates an additional screen to tell the user that the username they entered was incorrect, does not destroy the login screen
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")

    Label(screen5, text="User not found").pack()
    Button(screen5, text="Ok", command=delete5).pack()

#Main screen that holds the login and register buttons
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x400")
    screen.title("Email Login")

    header = tk.Label(text="Login/Register Below", bg="grey", fg="black",
                      height="2", width="100", font=("Times", 13)).pack()

    Label(text="").pack()
    start_login = tk.Button(text="Login", bg="white", fg="black",
                            height="2", width="20", command=login).pack()
    start_register = tk.Button(text="Register", bg="white", fg="black",
                               height="2", width="20", command=register).pack()

    screen.mainloop()


main_screen()