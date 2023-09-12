from GUI import *

usuarioAceptado= False
nUsuario= ""

while(True):
    if usuarioAceptado:
        print(f"Usuario {nUsuario} aceptado")
        app = App()
        app.mainloop()
        print("cerrando")
        usuarioAceptado= False
        break
    else:
        nUsuario= ""
        ILogin= Interfazlogin()
        print("iniciando ventana de login")
        ILogin.mainloop()
        print("ventana de login cerrada")
        usuarioAceptado= ILogin.usuarioA
        nUsuario= ILogin.usuario
        if ILogin.cerrar:
            break




exit()