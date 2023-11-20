import customtkinter
from customtkinter import CTk, CTkFrame

def calcular_suma():
    try:
        # Obtener los valores ingresados por el usuario
        miu = float(entry1.get())
        landa = float(entry2.get())
        ele_ant = float(entry3.get())

        # Obtener la probabilidad de que el cliente tenga (o no) que esperar
        proba_posi = landa / miu 
        proba_neg = 1-(landa/miu)

        #Verificar si lambda es mayor o menor que miu

        if landa > miu:
            wq = landa/(miu*(miu-landa))
        else:
            wq = miu

        lq = landa*wq #lq numero promedio de clientes

        ls = landa/(miu-landa) #ls promedio de cleintes en cola

        ws = ls/landa #ws tiempo espera por lciente en el sistema

        esp = (1-(landa/miu))*(landa/miu)

        esp_el = (1-(landa/miu))*((landa/miu)**ele_ant)

        spec = esp * 100
        spec_el = esp_el * 100
            
        result1.delete(0, customtkinter.END)  
        result1.insert(0, lq)  
        result2.delete(0, customtkinter.END)  
        result2.insert(0, ls)  
        result3.delete(0, customtkinter.END)  
        result3.insert(0, ws)  
        result4.delete(0, customtkinter.END)  
        result4.insert(0, spec) 
        result5.delete(0, customtkinter.END)  
        result5.insert(0, spec_el) 

        

    except ValueError:
        result1.delete(0, customtkinter.END)  # Limpiar el campo de entrada
        result1.insert(0, "Error: Ingrese números válidos")
        result2.delete(0, customtkinter.END)  # Limpiar el campo de entrada
        result2.insert(0, "Error: Ingrese números válidos")
        result3.delete(0, customtkinter.END)  # Limpiar el campo de entrada
        result3.insert(0, "Error: Ingrese números válidos")
        result4.delete(0, customtkinter.END)  # Limpiar el campo de entrada
        result4.insert(0, "Error: Ingrese números válidos")
        result5.delete(0, customtkinter.END)  # Limpiar el campo de entrada
        result5.insert(0, "Error: Ingrese números válidos")
      
    

root = CTk()
root.title("I.O Colas")
root.geometry('1000x1000+350+25')
root.minsize(480,500)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Resolucion de problemas de colas")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Capacidad de atencion del sistema: ")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Media de llegada: ")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Elementos: ")
entry3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Calcular", command=calcular_suma)
button.pack(pady=12, padx=10)

result = customtkinter.CTkLabel(master=frame, text="Resultados")
result.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Numero promedio de clientes: ")
label.pack(pady=12, padx=10)

result1 = customtkinter.CTkEntry(master=frame, placeholder_text=" ")
result1.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Promedio de clientes en la cola: ")
label.pack(pady=12, padx=10)

result2 = customtkinter.CTkEntry(master=frame, placeholder_text=" ")
result2.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Tiempo de espera por cliente en el sistema: ")
label.pack(pady=12, padx=10)

result3 = customtkinter.CTkEntry(master=frame, placeholder_text=" ")
result3.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Probabilidad de que el sistema este ocupado por lo menos con un cliente: ")
label.pack(pady=12, padx=10)

result4 = customtkinter.CTkEntry(master=frame, placeholder_text=" ")
result4.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Probabilidad de que haya n numero de elementos antes en la cola: ")
label.pack(pady=12, padx=10)

result5 = customtkinter.CTkEntry(master=frame, placeholder_text=" ")
result5.pack(pady=12, padx=10)

root.mainloop()