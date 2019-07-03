from tkinter import *


tk = Tk() 

canvas = Canvas(tk,width=1200, height=900, bg= 'black')
canvas.pack(expand=YES, fill=BOTH)
tk.title("*Juego de Damas*")


def crear_tablero():    
    for x in range(32):
        canvas.create_rectangle(0,0,100,100, fill='gray')        
    for a in range(4):
        canvas.move(a+1,(a)*200,0)
    for b in range(4):
        canvas.move(b+5,(b+(b+1))*100,100)
    for a in range(4):        
        canvas.move(a+9,(a)*200,200)
    for b in range(4):
        canvas.move(b+13,(b+(b+1))*100,300)
    for a in range(4):        
        canvas.move(a+17,(a)*200,400)
    for b in range(4):
        canvas.move(b+21,(b+(b+1))*100,500)
    for a in range(4):        
        canvas.move(a+25,(a)*200,600)
    for b in range(4):
        canvas.move(b+29,(b+(b+1))*100,700)

def crear_fichas():
	for x in range(12):
		p_roja = canvas.create_oval(0,0,100,100, fill='red')
	for a in range(4):
		canvas.move(a+33,(a)*200,0)
	for b in range(4):
		canvas.move(b+37,(b+(b+1))*100,100)
	for a in range(4):
		canvas.move(a+41,(a)*200,200)
	for x in range(12):
		p_blanca = canvas.create_oval(0,0,100,100, fill='white')
	for b in range(4):
		canvas.move(b+45,(b+(b+1))*100,500)
	for a in range(4):
		canvas.move(a+49,(a)*200,600)
	for b in range(4):
		canvas.move(b+53,(b+(b+1))*100,700)

puntNeg = 0
puntBlnc = 0

	
def status(titulo,nombre):
	asignatura = canvas.create_text(800,30,text=' Programacion Avanzada', fill='yellow', anchor = W, font=("Algerian", "20"))
	nombre = canvas.create_text(800,60,text='Amoguimba Jessica',fill='yellow', anchor = W, font=("Helvetica", 20, "bold italic"))
	text_turno = canvas.create_text(800,600, text='Siguiente turno --->  ',fill='white', anchor = W, font=("Helvetica", 20, "bold italic"))
	ficha_aux = canvas.create_rectangle(1100,550,1190,650,fill='white')
    


num_ficha=56

def moverFicha(event):

    if event.keysym == 'Up':
        canvas.move(num_ficha, 0, -100)
        print(canvas.coords(num_ficha))

    elif event.keysym == 'Down':
        canvas.move(num_ficha, 0, 100)
        print(canvas.coords(num_ficha))
    elif event.keysym == 'Left':
        canvas.move(num_ficha, -100, 0)
        print(canvas.coords(num_ficha))
    else:
        canvas.move(num_ficha, 100, 0)
        print(canvas.coords(num_ficha))
  
   

canvas.bind_all('<KeyPress-Up>', moverFicha)
canvas.bind_all('<KeyPress-Down>', moverFicha)
canvas.bind_all('<KeyPress-Left>', moverFicha)
canvas.bind_all('<KeyPress-Right>', moverFicha)

def clickFicha(event):
    
    fila = (8*event.y)//600
    columna =(8*event.x)//600
    global movimientos
    global labelFichaSeleccionada
    movimientos.append([fila,columna])
    if len(movimientos)==1:
        labelMovimientoInvalido.place_forget()
        x = columna*75+32
        y = fila*75+32
        x1 = x+10
        y1= y+10
        labelFichaSeleccionada = tableroGUI.create_oval(x,y,x1,y1,fill="blue")
    if len(movimientos)==2:
        tableroGUI.delete(labelFichaSeleccionada)
        valor = validarMovimiento(movimientos[0],movimientos[1])
        movimientos = []
        if valor==True:
            pintarTablero()
            pintarTableroFichas(tablero)
        else:
            labelMovimientoInvalido.place(x="625",y="250")


crear_tablero()
crear_fichas()
status(puntNeg,puntBlnc)




tk.mainloop()

