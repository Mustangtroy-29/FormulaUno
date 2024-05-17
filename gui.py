import customtkinter
from customtkinter import *
from my_package import driver_data

app = CTk()
app.title("Formula Uno")
app.geometry("600x650")

my_combobox2 = CTkComboBox(app, values=driver_data.season)
my_combobox2.pack(pady=20)


my_combobox1 = CTkComboBox(app, values=driver_data.drivers)
my_combobox1.pack(pady=60)



app.mainloop()

