from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
from pyttsx3 import init
from pywhatkit import search, playonyt, sendwhatmsg
import datetime as dt
from wikipedia import page, summary, set_lang
from time import sleep
from webbrowser import open_new_tab
from os import rmdir, mkdir, linesep
import errno
from subprocess import run, Popen
from pyautogui import hotkey
from random import choice

# Variables del bot
name = 'cortana'
listener = sr.Recognizer()

engine = init()

# Voz del bot
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

# Funcion hablar
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Funcion para ejecutar comandos del cmd
def cmd(commando):
    run(commando, shell=True)

# Funcion para que me oiga y reconozca
def listen():
    global rec
    try:
        with sr.Microphone(device_index=1) as micro:
            talk('Te escucho...')
            print('Escuchando...')
            voice = listener.listen(micro)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')

            print(rec)
    except:
        pass
    return rec

# Diccionarios y listas
saludo = ['buenos días', 'buenas tardes', 'buenas noches', 'hola', 'qué onda', 'cómo andas', 'qué tal', 'que tal']
sites = {
    'google' : 'google.com',
    'facebook' : 'facebook.com',
    'youtube' : 'youtube.com',
    'whatsapp' : 'web.whatsapp.com'
}

folders = {
    'lenin' : r'start %windir%\explorer.exe D:\Lenin Castro\Carpetas de Escritorio\Lenin',
    'programar' : r'start %windir%\explorer.exe D:\Lenin Castro\Carpetas de Escritorio\programar',
    'cuarto de secundaria' : r'start %windir%\explorer.exe D:\Lenin Castro\Carpetas de Escritorio\CuartoDeSecundaria'
}

programs = {
    'el navegador' : r'start msedge.exe',
    'epic' : r'D:\Games\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe',
    'discord' : r'C:\Users\Lenin Castro\AppData\Local\Discord\app-1.0.9001\Discord.exe',
    'juego otaku' : r'D:\Games\Genshin Impact\launcher.exe',
    'vs code' : r'C:\Users\Lenin Castro\AppData\Local\Programs\Microsoft VS Code\Code.exe',
    'editor de código de python' : r'D:\Program Files\PyCharm Community Edition 2021.1.1\bin\pycharm64.exe'
}

def write(f):
    talk('¿Qué quieres que escriba?')
    rec_write = listen()
    f.write(rec_write + linesep)
    f.close()
    talk('Listo, puedes revisarlo')
    Popen(r'C:\Users\Lenin Castro\Desktop\nota.txt', shell = True)

# Funcion para que corra el bot
def run_assist():
    rec = listen()
    rec = rec.strip()
    if 'reproduce' in rec:  # Reproduce algo en Youtube
        music = rec.replace('reproduce', ' ')
        talk('Reproduciendo' + music)
        playonyt(music)
    elif 'hora' in rec:  # Da la hora
        hora = dt.datetime.now().strftime('%H:%M ')
        talk('Son las' + hora)
    elif 'busca en wikipedia' in rec:  # Buscar algo en Wikipedia
        set_lang("es")
        order = rec.replace('busca en wikipedia', '')
        order = order.strip()
        info = summary(order, 1)
        talk('Buscando' + order + 'en Wikipedia')
        sleep(1)
        open_new_tab(page(order).url)
        talk(info)
    elif 'busca' in rec:  # Busca algo en google
        google = rec.replace('busca', '')
        search(google)
        talk('Buscando' + google)
    elif 'envía un mensaje diciendo' in rec:  # Enviar mensaje por WhatsApp
        hour = int(dt.datetime.now().strftime('%H'))
        minute = int(dt.datetime.now().strftime('%M')) + 1.1
        whats = rec.replace('envía un mensaje diciendo', '')
        whats1 = str(whats)
        talk('¿A qué numero quieres enviar el mensaje?')
        new = listen()
        phone_number = new.strip()
        sendwhatmsg(f'+51{phone_number}', whats1, hour, minute, 8)
    elif 'abre' in rec:  # Abrir Carpetas o programas
        open_program = rec.replace('abre', '')
        final_open = open_program.strip()

        if sites.get(final_open) or folders.get(final_open) or programs.get(final_open) is not None:
            for site in sites:
                if site in rec:
                    comando = f'start msedge.exe {sites[site]}'
                    cmd(comando)
                    talk(f'Abriendo {site}')
            for program in programs:
                if program in rec:
                    comando = programs[program]
                    cmd(comando)
                    talk(f'Abriendo {program}')
            for folder in folders:
                if folder in rec:
                    comando = folders[folder]
                    cmd(comando)
                    talk(f'Abriendo {folder}')
        else:
            print(f'No existe el programa o carpeta {final_open}')
            talk(f'No existe el programa o carpeta {final_open}')

    elif 'escribe' in rec: # Escribir en el bloc de notas
        try:
            with open(r'C:\Users\Lenin Castro\Desktop\nota.txt', 'a') as f:
                write(f)
        except FileNotFoundError:
            file = (r'C:\Users\Lenin Castro\Desktop\nota.txt', 'w')
            write(file)

    elif 'crea una carpeta llamada' in rec:  # Crear carpeta
        name_cap = rec.replace('crea una carpeta llamada', '')
        final_name_cap = name_cap.strip()

        try:
            mkdir(fr'C:\Users\Lenin Castro\Desktop\{final_name_cap}')
            talk('Creando carpeta')
            sleep(1)
            talk('Carpeta creada exitosamente')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    elif 'elimina la carpeta llamada' in rec:  # Eliminar carpeta
        name_cap_delete = rec.replace('elimina la carpeta llamada', '')
        final_name = name_cap_delete.strip()

        try:
            rmdir(fr'C:\Users\Lenin Castro\Desktop\{final_name}')
            print('Eliminando carpeta')
            talk('Eliminando carpeta')
            sleep(1)
            print(f'Carpeta {final_name} eliminada correctamente')
            talk(f'Carpeta {final_name} eliminada correctamente')
        except:
            print('No hay ninguna carpeta llamada así')
            talk('No hay ninguna carpeta llamada así')

    elif 'captura' in rec:  # Capturar pantalla
        try:
            hotkey('shift', 'printscreen')
            sleep(5)
            hotkey('alt', 'printscreen')
            talk('Realizando captura...')
            sleep(1)
            talk('Capturas hechas')
        except:
            pass
    # Saludar
    elif 'buenos días' or 'buenas tardes' or 'buenas noches' or 'hola' or 'qué onda' or 'cómo andas' or 'qué tal' in rec:
        final_rec_saludo = rec.strip()
        saludos_bot = ['Hola, cómo andas', 'Qué tal, Lenin', '¡Hey, hola!',
                       'Hola, espero tengas o hayas tenido un buen día']
        for i in saludo:
            final_saludos_bot = choice(saludos_bot)
            if i.strip() == final_rec_saludo:
                talk(final_saludos_bot)
                print(final_saludos_bot)
    else:
        talk('Lo siento no tengo alguna respuesta para eso')
        print('Lo siento no tengo alguna respuesta para eso')

# INTERFAZ GRÁFICA
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

boton_archivos = Button(main_window, text="Agregar archivos", bg='#16222A', fg="white", font=('Arial', 16, 'bold'))
boton_archivos.place(x=1075, y=150, height=40, width=200)

boton_webs = Button(main_window, text="Agregar páginas", bg='#16222A', fg="white", font=('Arial', 16, 'bold'))
boton_webs.place(x=1075, y=200, height=40, width=200)

boton_programs = Button(main_window, text="Agregar programas", bg='#16222A', fg="white", font=('Arial', 16, 'bold'))
boton_programs.place(x=1075, y=250, height=40, width=200)

boton_add_files = Button(main_window, text="Archivos agregados", bg='#474747', fg="white", font=('Arial', 14, 'bold'))
boton_add_files.place(x=1075, y=300, height=40, width=200)

boton_add_webs = Button(main_window, text="Páginas agregadas", bg='#474747', fg="white", font=('Arial', 14, 'bold'))
boton_add_webs.place(x=1075, y=350, height=40, width=200)

boton_add_programs = Button(main_window, text="Apps agregadas", bg='#474747', fg="white", font=('Arial', 14, 'bold'))
boton_add_programs.place(x=1075, y=400, height=40, width=200)

main_window.mainloop()