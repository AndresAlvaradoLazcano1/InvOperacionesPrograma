from tkinter import DoubleVar #jaja no se porque se agregaron estas no le se a phyton me estresa
from tokenize import Double

#datos a pedir
miu = Double(input("Capacidad de atencion: ")) #capacidad de atencion
landa = Double(input("Media de llegada: ")) #media de llegada
ele_ant = int(input("Elementos: ")) #pedir cuando el usuario quiera saber la probabilidad de encontrarse con n numero de elementos antes en la cola

#FORMULAS
proba_posi = landa/miu #probabilidad positiva en caso de que si tenga espera
proba_neg = 1-(landa/miu) #probabilidad negativa en caso de no esperar

if landa>miu : #Wq tiempo espera clientes cola
  wq = landa/(miu(miu-landa))
else :
  wq = miu

lq = landa*wq #lq numero promedio de clientes

ls = landa/(miu-landa) #ls promedio de cleintes en cola

ws = ls/landa #ws tiempo espera por lciente en el sistema

#probabilidad de que el sitema este ocupado por lo menos 1
esp = (1-(landa/miu))*(landa/miu)

#probabilidad de que haya n numero de elemntos antes en la cola
esp_el = (1-(landa/miu))*((landa/miu)**ele_ant)