from customtkinter import *

def main():
	app= CTk()
	app.geometry("1920x1080")
	btn=CTkButton(master=app, text="Click Me")
	btn.place(relx=0.5, rely=0.5, anchor="center")
	app.mainloop()

if __name__ == '__main__':
	main()