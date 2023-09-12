import ktinker
import customtkinter #https://customtkinter.tomschimansky.com/documentation/

#customtkinter.set_default_color_theme("dark-blue.json")

def hola():
    print("hola")

def boton1():
    label.configure(text= entry.get())

root= customtkinter.CTk()
root.title(":(")
customtkinter.set_appearance_mode("dark")

root.geometry("300x400")

entry = customtkinter.CTkEntry(root, placeholder_text="escriba aqui")
entry.place(relx= 0.5, rely= 0.5)

button= customtkinter.CTkButton(master=root, text="actualizar",state="normal",command= boton1)

button.place(relx= 0.5, rely= 0.5)

label = customtkinter.CTkLabel(master=root, text="", fg_color="transparent")
label.place(relx= 0.5, rely= 0.5)

root.mainloop()