import tkinter as tk
import tkinter.font as font
from tkinter import font as tkFont

# List
 
names_pws = {
    "Yousef": "Password"
}

# The creation of the base interface
 
root = tk.Tk()
root.title("Login")
lbl_font = font.Font(family='Georgia', size='15', weight='bold')
screen_width = 670
screen_height = 400
root.geometry('%dx%d+0+0' % (screen_width, screen_height))
root.configure(bg="darkblue")
label = tk.Label(root)
 
# Title label
 
lbl = tk.Label(root, font=lbl_font, fg='white', bg="blue", text='Welcome to All About Toys\n'
                                                                         'Please enter your username and password to access your account!')
lbl.pack()

 
# Function of the confirm button
 
def click_confirm():
    global label
    label.destroy()
    entered_pw = password.get()
    entered_un = username.get()
    if entered_un in names_pws:
        if entered_pw == names_pws[entered_un]:
            hello = "Hello " + username.get() + " , welcome back!"
            label = tk.Label(root, font=lbl_font, text=hello, bg="green", fg="lightyellow", borderwidth=5)
        else:
            hello = "Your password is incorrect!"
            label = tk.Label(root, font=lbl_font, text=hello, bg="brown", fg="lightyellow", borderwidth=5)
    else:
        if entered_un == "":
            label = tk.Label(root, font=lbl_font, text="Please enter username!", bg="brown", fg="lightyellow", borderwidth=5)
        else:
            label = tk.Label(root, font=lbl_font, text="Your username is incorrect!", bg="brown", fg="lightyellow", borderwidth=5)
    label.place(y=260, x=5)

 
# Labels, Buttons and entries for the login



btn = tk.Button(root, text='Exit',
                fg='darkblue', bg='darkgray',
                command=quit)
btn["font"]=lbl_font
btn.place(x=250, y= 300)


 
username_lbl = tk.Label(root, font=lbl_font, text="Username:", bg="white", fg="black", borderwidth=5)
username = tk.Entry(root, font=lbl_font, bg="royalblue", fg="lightyellow", borderwidth=5)
password_lbl = tk.Label(root, font=lbl_font, text="Password: ", bg="white", fg="black", borderwidth=5)
password = tk.Entry(root, font=lbl_font, bg="royalblue", fg="lightyellow", borderwidth=5)
confirm = tk.Button(root, font=lbl_font, text="Enter", command=click_confirm, borderwidth=5, bg="brown", fg="black")
lbl.place(x=0)
username_lbl.place(y=100, x=5)
password_lbl.place(y=150, x=5)
username.place(y=100, x=160)
password.place(y=150, x=160)
confirm.place(y=200, x=5)
 
# Running the interface


root.mainloop()
 
# End
