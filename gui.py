import customtkinter
from customtkinter import *
from my_package import driver_data

app = CTk()
app.title("Formula Uno")
app.geometry("600x650")

def clicker():
    my_progressbar.step()
    my_label.configure(text=(int(my_progressbar.get()*100)))

my_progressbar = CTkProgressBar(app, orientation="horizontal")
my_progressbar.pack(pady=40)
my_progressbar.set(0)

my_button = CTkButton(app, text="Click Me", command=clicker)
my_button.pack(pady=20)

my_label = CTkLabel(app, text='')
my_label.pack(pady=20)

app.mainloop()

