import tkinter
import customtkinter #https://customtkinter.tomschimansky.com/documentation/
import os
from pathlib import Path

from comados import *

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

icono= os.path.join(os.path.abspath(os.path.dirname(__file__)), "images.ico")

class Interfazlogin(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(icono)
        self.usuarioA= False
        self.usuario= ""
        self.cerrar= False
        
        
        self.geometry(f"{500}x{600}")
        
        #login
        self.title("Login")
        def Cerrar():
            if(login(self.entradaUsuario.get(),self.entradaContraseña.get())):
                self.usuarioA= True
                self.usuario= self.entradaUsuario.get()
                self.destroy()
            else:
                self.mensaje.configure(text= "El usuario o contraseña no coinciden")
        
        self.espacio= customtkinter.CTkLabel(master= self, text="",height=200)
        self.espacio.grid(row=0 , column= 0,padx=50, pady=5)
        
        self.mensaje= customtkinter.CTkLabel(master=self,text="")
        self.mensaje.grid(row=3, column= 0, padx=50, pady=5)
        
        self.entradaUsuario= customtkinter.CTkEntry(master=self, placeholder_text= "Usuario", height=60, width=400)
        self.entradaUsuario.grid(row=1, column=0, padx=50, pady=5)
        #self.entradaUsuario.place(rely= -10)
        
        self.entradaContraseña= customtkinter.CTkEntry(master=self, placeholder_text= "Contraseña", show="*", height=60, width=400)
        self.entradaContraseña.grid(row=2, column=0, padx=0, pady=5)
        self.entradaContraseña.bind("<Return>", Cerrar)
        
        self.boton= customtkinter.CTkButton(master=self,text= "Entrar", command= Cerrar, height=60, width=400)
        self.boton.grid(row=4, column=0, padx=0, pady=5)
        
        self.mensajeMotivacional= customtkinter.CTkLabel(master=self,text="15 años en la logistica de repartir tus sueños")
        self.mensajeMotivacional.grid(row=5, column= 0, padx=50, pady=5)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(icono)
        
        self.geometria= [int(self.winfo_screenwidth()*0.6),int(self.winfo_screenheight()*0.6)]
        self.geometry(f"{self.geometria[0]}x{self.geometria[1]}+{int(self.winfo_screenwidth()/2-self.geometria[0]/2)}+{int(self.winfo_screenheight()/2-self.geometria[1]/2)}")
        
        
        self.title("Sistema EXUN S.A.")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        #self.barraArriba= customtkinter.CTkFrame(self, height= 3, width= 3)
        #self.barraArriba.grid(row= 0, column= 0, sticky= "nsew")
        
        self.tab= customtkinter.CTkTabview(self)   # self.tab.tab("NOMBRE")
        self.tab.grid(row=0, column=0 , sticky="nsew", padx=0, pady= 0)
        self.grid_columnconfigure(1, weight= 1, pad=0)
        self.grid_rowconfigure(1, weight= 1)
        
        
        
        # stock
        self.tab.add("Stock")
        self.tab.tab("Stock").grid_columnconfigure(0, weight=1)
        
        self.cuadroStock= customtkinter.CTkScrollableFrame(self.tab.tab("Stock"), width= 500, label_anchor= "center") #boton para pedir stock
        self.cuadroStock.grid(row=0, column= 0)
        
        for numeroOrden in range(cantTiposStock()): #agrega una etiqueta por cada uno de los empleados
            datosOrden= stockN(numeroOrden)
            locals()["stock" + str(datosOrden)]= customtkinter.CTkLabel(self.cuadroStock, text= f"tipo: {datosOrden[0]}  cantidad: {datosOrden[1]}")
            locals()["stock" + str(datosOrden)].grid(row= numeroOrden, column= 0)
        
        self.textoPedirStock= customtkinter.CTkLabel(self.tab.tab("Stock"), text="")
        self.textoPedirStock.grid(row= 1, column= 0)
        
        def cambiarTextoPedirStock():
            self.textoPedirStock.configure(text= "Stock Pedido, aguarde 24hs para el impacto en el sistema")
        
        self.botonPedirStock= customtkinter.CTkButton(self.tab.tab("Stock"), text="pedir stock" , command= cambiarTextoPedirStock)
        self.botonPedirStock.grid(row= 2, column= 0)
        
        
        
        # Revisa pedidos
        self.tab.add("Revisar Pedidos")
        
        
        self.pedidoFrame= customtkinter.CTkFrame(self.tab.tab("Revisar Pedidos"))
        self.pedidoFrame.grid(row= 1, column= 0)
        
        
        
        self.entradaPedido= customtkinter.CTkEntry(self.pedidoFrame)
        self.entradaPedido.grid(row= 0, column= 0)
        
        self.nombreCliente= customtkinter.CTkLabel(self.tab.tab("Revisar Pedidos"), text="")
        self.nombreCliente.grid(row= 2, column= 0)
        
        self.descripcionEntrega= customtkinter.CTkFrame(self.tab.tab("Revisar Pedidos"))
        self.descripcionEntrega.grid(row= 3, column= 0)
        
        self.tipoDeColchon= customtkinter.CTkLabel(self.descripcionEntrega, text="")
        self.tipoDeColchon.grid(row= 0, column= 0)
        
        self.cantidadDeColchones= customtkinter.CTkLabel(self.descripcionEntrega, text="")
        self.cantidadDeColchones.grid(row= 0, column= 1)
        
        self.destino= customtkinter.CTkLabel(self.tab.tab("Revisar Pedidos"), text="")
        self.destino.grid(row= 4, column= 0)

        self.tiempoEstimado= customtkinter.CTkLabel(self.tab.tab("Revisar Pedidos"), text="")
        self.tiempoEstimado.grid(row= 5, column= 0)

        self.costoDeTransporte= customtkinter.CTkLabel(self.tab.tab("Revisar Pedidos"), text="")
        self.costoDeTransporte.grid(row= 6, column= 0)
        
        self.error= customtkinter.CTkLabel(self.tab.tab("Revisar Pedidos"), text="")
        self.error.grid(row= 0, column= 0)
        
        def cambiarDetallesDeEnvio():
            numeroDeEnvio= int(self.entradaPedido.get())-1
            if cantEnvios()<numeroDeEnvio:
                self.error.configure(text= f"error, solo hay {cantEnvios()} envios")
                return
            
            self.error.configure(text= "")
            datosDePedido= pedidoN(numeroDeEnvio)
            self.nombreCliente.configure(text= f"nombre: {datosDePedido[3]}")
            self.tipoDeColchon.configure(text= f"tipo de colchon: {datosDePedido[1]} |")
            self.cantidadDeColchones.configure(text= f"| cantidad: {datosDePedido[2]}")
            self.destino.configure(text= f"destino: {datosDePedido[0]}")
            self.tiempoEstimado.configure(text= f"tiempo estimado: {datosDePedido[4]}")
            self.costoDeTransporte.configure(text= f"costo de envio: {datosDePedido[5]}")

        
        self.botonActualizarPedido= customtkinter.CTkButton(self.pedidoFrame, text="Actualizar Datos", command= cambiarDetallesDeEnvio)
        self.botonActualizarPedido.grid(row= 0, column= 1)
        
        
        
        
        # registro de pagos
        self.tab.add("Pagos")

        self.pagosFrame= customtkinter.CTkFrame(self.tab.tab("Pagos"))
        self.pagosFrame.grid(row= 0, column= 0)

        self.entradapago= customtkinter.CTkEntry(self.pagosFrame)
        self.entradapago.grid(row= 0, column= 0)

        self.nombreClientePagos= customtkinter.CTkLabel(self.tab.tab("Pagos"), text="")
        self.nombreClientePagos.grid(row= 1, column= 0)

        self.numeroDePedido= customtkinter.CTkLabel(self.tab.tab("Pagos"), text="")
        self.numeroDePedido.grid(row= 2, column= 0)

        self.cantidadPagada=customtkinter.CTkLabel(self.tab.tab("Pagos"), text="")
        self.cantidadPagada.grid(row= 3, column= 0)


        def cambiarDetallesDePago():
            datosDePago= pagoN(int(self.entradapago.get())-1)
            self.nombreClientePagos.configure(text= f"nombre: {datosDePago[0]}")
            self.numeroDePedido.configure(text= f"pedido N°{datosDePago[1]}")
            self.cantidadPagada.configure(text= f"cantidad pagada: ${datosDePago[2]}")


        self.botonActualizarPago= customtkinter.CTkButton(self.pagosFrame, text="Actualizar pagos", command= cambiarDetallesDePago)
        self.botonActualizarPago.grid(row= 0, column= 1)
        
        # registro entrada y salida de empleados
        self.tab.add("Empleados")
        self.tab.tab("Empleados").grid_columnconfigure(1, weight= 1, pad=0)
        self.tab.tab("Empleados").grid_rowconfigure(1, weight= 1)
        
        # frame con la entrada y salida de un empleado especifico
        self.frameEmpleado= customtkinter.CTkFrame(self.tab.tab("Empleados"))
        self.frameEmpleado.grid(row= 0, column= 1)
        
        self.nombreEmpleado= customtkinter.CTkLabel(self.frameEmpleado, text="Horarios del empleado:")
        self.nombreEmpleado.grid(row=0, column= 0)
        
        self.HorariosDeEmpleado= customtkinter.CTkScrollableFrame(self.frameEmpleado, fg_color="#262626")
        self.HorariosDeEmpleado.grid(row= 1, column= 0)
        
        
        
        def agregarHorariosEmpleado(numero):
            self.HorariosDeEmpleado.destroy()
            self.HorariosDeEmpleado= self.HorariosDeEmpleado= customtkinter.CTkScrollableFrame(self.frameEmpleado, fg_color="#262626")
            self.HorariosDeEmpleado.grid(row= 1, column= 0)
            self.nombreEmpleado.configure(text= nombreEmpleado(numero= numero))
            lista= horariosEmpleado(numero= numero)
            for i in range(len(lista)):
                locals()["empleado" + str(i)]= customtkinter.CTkLabel(self.HorariosDeEmpleado, text= lista[i])
                locals()["empleado" + str(i)].grid(row= i, column= 0)
            print("Lista de horarios actualizada, empleado N: ", numero)
        
        
        # Frame con los nombres de los empreados
        self.empleados= customtkinter.CTkScrollableFrame(self.tab.tab("Empleados"))
        self.empleados.grid(row= 0, column= 0)
        self.empleados.grid_columnconfigure(0, weight=1)
        for nEmpleado in range(cantEmpleados()): #agrega una etiqueta por cada uno de los empleados
            locals()["empleado" + str(nEmpleado)]= customtkinter.CTkButton(self.empleados, text=nombreEmpleado(nEmpleado) ,command= lambda i=nEmpleado: agregarHorariosEmpleado(i))
            locals()["empleado" + str(nEmpleado)].grid(row= nEmpleado, column= 0)
        