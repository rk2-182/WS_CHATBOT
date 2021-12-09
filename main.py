"""
09-12-21
==========================================
*PyAutoGUI: es un módulo para automatizar tareas en múltiples sistemas operativos. «Automatizar» es generalmente entendido como controlar el mouse
    y el teclado, aunque en este caso en particular se incluyen otras herramientas como cuadros de diálogo y capturas de pantalla.



"""
#importar librerias para el proyecto
import pyautogui
from pynput import mouse
import pyperclip
from pynput.mouse import Button, Controller
import time
import os

pyautogui.FAILSAFE = True
mouse = Controller()


def nav_to_image(image, clicks, off_x=0,off_y=0):
    posicion = pyautogui.locateCenterOnScreen(image,confidence=.8)

    if posicion is None:
        print("{0} no encontrada...".format(image))
    else:
        print("Encontrado!")
        pyautogui.moveTo(posicion, duration=.5)
        pyautogui.moveRel(off_x, off_y,duration=.2)
        pyautogui.click(clicks=clicks, interval=.1)

"""
time.sleep(4)

nav_to_image('img/clip.JPG',0)
nav_to_image('img/equis.JPG',0)
nav_to_image('img/notificacion.JPG',0)
nav_to_image('img/copia.png',0)
"""

def get_message():
    nav_to_image('img/clip.png',0, off_y=-65) #buscar clip ws
    mouse.click(Button.left,3)
    pyautogui.rightClick()

    copy =nav_to_image('img/copia.png',1)
    time.sleep(.5)

    return pyperclip.paste() if copy !=0 else 0 #copiar en el portapapeles si es disinto de 0 copiara sino retora 0

#escribir un mensaje
def send_message(msg):
    nav_to_image('img/clip.png',2,off_x=100) #mover a la derecha 100 px
    pyautogui.typewrite(msg, interval=.1)
    pyautogui.typewrite('\n') #simular ENTER

#Cerrar cuadro de respuesta ws
def close_reply_box():
    nav_to_image('img/equis.JPG',2)


def process_message(msg):
    raw_msg = msg.lower()

    if raw_msg == 'hola' or raw_msg == 'Hola':
        return 'Hola!, ¿en que puedo ayudarte?'
    elif raw_msg == 'buenas':
        return "ola ke ase?"
    else:
        return 'No entiendo lo que me estas diciiendo ._.'



time.sleep(2)
#print(get_message())
#close_reply_box()
#send_message('Mensaje de Prueba.')

#os.system('cls')
#print(process_message('hhfgh'))

#Loop
delay = 10
last_message =''


time.sleep(3)
while True:
    #Buscar nuevos mensajes en ws (buscar punto verde y moverse 100px a izq.)
    nav_to_image('img/notificacion.JPG',2,off_x=-100) #1
    close_reply_box() #2

    message = get_message() # 3

    if message != 0 and message != last_message:
        last_message = message
        send_message(process_message(message))
    else:
        print("No hay mensajes...")
    
    pyautogui.sleep(10)


