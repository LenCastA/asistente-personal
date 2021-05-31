from tkinter import *
from PIL import Image, ImageTk

# Funciones especiales de la interfaz
def talk_anything():
    text = text_info.get("1.0", "end")
    talk(text)

def write_text(textc):
    text_info.insert(INSERT, textc)

def add_file_graph():
    global namef_entry, rutef_entry
    file_win = Toplevel()
    file_win.title("Agregar archivos")
    file_win.geometry('400x200')
    file_win.configure(bg="#434343")
    file_win.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(file_win)} center')
    title_label = Label(file_win, text="Agrega un archivo", fg="white", bg="#434343", font=('Arial', 15, 'bold')).pack(pady=5)
    text_name = Label(file_win, text="Nombre del archivo", fg="white", bg="#434343", font=('Arial', 12, 'bold')).pack(pady=3)
    namef_entry = Entry(file_win)
    namef_entry.pack(pady=2)
    text_rute = Label(file_win, text="Ruta del archivo", fg="white", bg="#434343", font=('Arial', 12, 'bold')).pack(pady=3)
    rutef_entry = Entry(file_win, width=30)
    rutef_entry.pack(pady=2)
    Button(file_win, text="Agregar", bg='#16222A', fg="white", width=10, height=1).pack(pady=5)

def add_web_graph():
    global namef_entry, rutef_entry
    file_win = Toplevel()
    file_win.title("Agregar archivos")
    file_win.geometry('400x200')
    file_win.configure(bg="#434343")
    file_win.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(file_win)} center')
    title_label = Label(file_win, text="Agrega una web", fg="white", bg="#434343", font=('Arial', 15, 'bold')).pack(pady=5)
    text_name = Label(file_win, text="Nombre de la web", fg="white", bg="#434343", font=('Arial', 12, 'bold')).pack(pady=3)
    namew_entry = Entry(file_win)
    namew_entry.pack(pady=2)
    text_rute = Label(file_win, text="Link de la web", fg="white", bg="#434343", font=('Arial', 12, 'bold')).pack(pady=3)
    rutew_entry = Entry(file_win, width=30)
    rutew_entry.pack(pady=2)
    Button(file_win, text="Agregar", bg='#16222A', fg="white", width=10, height=1).pack(pady=5)

def add_program_graph():
    global namef_entry, rutef_entry
    file_win = Toplevel()
    file_win.title("Agregar archivos")
    file_win.geometry('400x200')
    file_win.configure(bg="#434343")
    file_win.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(file_win)} center')
    title_label = Label(file_win, text="Agrega un programa", fg="white", bg="#434343", font=('Arial', 15, 'bold')).pack(pady=5)
    text_name = Label(file_win, text="Nombre del programa", fg="white", bg="#434343", font=('Arial', 12, 'bold')).pack(pady=3)
    namep_entry = Entry(file_win)
    namep_entry.pack(pady=2)
    text_rute = Label(file_win, text="Ruta del programa", fg="white", bg="#434343", font=('Arial', 12, 'bold')).pack(pady=3)
    rutep_entry = Entry(file_win, width=30)
    rutep_entry.pack(pady=2)
    Button(file_win, text="Agregar", bg='#16222A', fg="white", width=10, height=1).pack(pady=5)

def add_file():


comandos = """ 
Comandos que puedes usar:
- Reproduce..(canción)
- Busca... (algo)
- Envía un mensaje diciendo... (mensaje)
- Busca en wikipedia...(algo)
- Abre...(web, programa o carpeta)
- Escribe... (la nota)
- Crea una carpeta llamada... (nombre)
- Elimina la carpeta llamada... (nombre)
- Toma una captura
- Qué hora es
- Termina
"""
# Ventana principal
main_window = Tk()
main_window.title('Asistente Virtual')

main_window.iconbitmap('recurses/av1.ico')
main_window.geometry('1366x720')
main_window.resizable(True, True)
main_window.config(bg = '#2C5364')

# Label e imagen del asistente
label_title = Label(main_window, text = 'Asistente Virtual', bg = '#2C5364', fg = '#E0E0E0', font = ('Arial', 30, 'bold'))
label_title.pack(pady = 10)

microphoto = ImageTk.PhotoImage(Image.open('recurses/main1.png'))
windows_photo = Label(main_window, image = microphoto, height = 500, width = 500).pack(pady = 10)

# Lista de comandos
listaComandos = Canvas(bg = '#2C5364', height = 300, width = 400)
listaComandos.place(x = 0, y = 0)
listaComandos.create_text(190, 140, text = comandos, fill = 'white', font = 'Arial 15')

# Donde se mostrará lo que digo y lo que el bot dice
text_info =Text(main_window, bg = '#2C5364', fg = 'white', bd = 2, font = ('Arial', 15))
text_info.place(x = 0, y = 306, height = 300, width = 404)

# Botones
boton1 = Button(main_window, text = 'Iniciar', width = 10, font = ('Arial', 16))
boton1.pack(pady = 10)

boton_hablar = Button(main_window, text="Hablar", bg='#b6fbff', fg="black", font=('Arial', 16, 'bold'))
boton_hablar.place(x=1100, y=100, height=40, width=150)

boton_archivos = Button(main_window, text="Agregar archivos", bg='#16222A', fg="white", font=('Arial', 16, 'bold'), command = add_file_graph)
boton_archivos.place(x=1075, y=150, height=40, width=200)

boton_webs = Button(main_window, text="Agregar páginas", bg='#16222A', fg="white", font=('Arial', 16, 'bold'), command = add_web_graph)
boton_webs.place(x=1075, y=200, height=40, width=200)

boton_programs = Button(main_window, text="Agregar programas", bg='#16222A', fg="white", font=('Arial', 16, 'bold'), command = add_program_graph)
boton_programs.place(x=1068, y=250, height=40, width=215)

boton_add_files = Button(main_window, text="Archivos agregados", bg='#474747', fg="white", font=('Arial', 14, 'bold'))
boton_add_files.place(x=1075, y=300, height=40, width=200)

boton_add_webs = Button(main_window, text="Páginas agregadas", bg='#474747', fg="white", font=('Arial', 14, 'bold'))
boton_add_webs.place(x=1075, y=350, height=40, width=200)

boton_add_programs = Button(main_window, text="Programas agregados", bg='#474747', fg="white", font=('Arial', 14, 'bold'))
boton_add_programs.place(x=1068, y=400, height=40, width=215)

main_window.mainloop()