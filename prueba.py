# Interfaz
def interfaz():
    root = Tk()

    root.iconbitmap('recurses/av1.ico')  # Icono de la ventana
    root.config(bg='gray57')  # Color de fondo
    root.title('Asistente Virtual Personal')
    root.geometry('1366x720')

    img = PhotoImage(file='recurses/main.png')
    botonNuevo1 = Button(root, image=img, compound="top", command=run_assist)
    botonNuevo1.place(x=400, y=100)

    root.mainloop()