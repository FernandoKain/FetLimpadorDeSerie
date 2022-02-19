# Bibliotecas a serem usadas
import pyautogui
import time

# pyautogui.click(x=713, y=700)

# Solicita entrada do usuário em relação ao número de atividades entregues.
# var = int(input("Insira o número de alunos que entregaram as atividades: "))


# Funções para otimizar o código
def alttab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def controlc():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

def alttab2():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def f2():
    pyautogui.press('f2')

def controlv():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')

def enter():
    pyautogui.press('enter')

def down():
    pyautogui.press("down")

def up():
    pyautogui.press("up")

def right():
    pyautogui.press("right")

def left():
    pyautogui.press('left')

def backspace():
    pyautogui.press('backspace')

def delete():
    pyautogui.press('delete')

def end():
    pyautogui.press('end')

def space():
    pyautogui.press('space')

def tab():
    pyautogui.press('tab')

def home():
    pyautogui.press('home')

# -------------Código começa------------------------

# -------------Ajuste das janelas-------------------
alttab()
time.sleep(0.5)

# Utilizar o localizar primeiro e substituir os itens desnecessário para depois usar o código

# for i in range(12):
#     for i in range(44):
#         f2()
#         up()
#         up()
#         delete()
#         up()
#         end()
#         backspace()
#         enter()
#     for i in range(44):
#         up()
#     right()



# ----------RoboWord-----------------


##----------- RoboWord Noit ------------
# for i in range(1):
#     for i in range(35):
#         end()
#         backspace()
#         space()
#         down()
#
#     for i in range(36):
#         up()
#
#     tab()
#     down()
#     down()


#----------- RoboWord Manhã Tarde------------
# for i in range(12):
#     for i in range(44):
#         end()
#         backspace()
#         space()
#         down()
#
#     for i in range(45):
#         up()
#
#     tab()
#     down()

# for i in range(5):
#     end()
#     backspace()
#     space()
#     down()
#
#     end()
#     backspace()
#     space()
#     down()
#
#     end()
#     backspace()
#     space()
#     down()
#
#     end()
#     backspace()
#     space()
#     down()
#
#     down()
#
#     end()
#     backspace()
#     space()
#     down()
#
#     end()
#     backspace()
#     space()
#     down()
#
#     end()
#     backspace()
#     space()
#     down()
#
#     down()



# Limpador de série 1

# for i in range(12):
#     for i in range(44):
#         f2()
#         up()
#         up()
#         up()
#         backspace()
#         backspace()
#         backspace()
#         delete()
#         enter()
#     for i in range(44):
#         up()
#     right()

# Limpador de Série 2
# for i in range(12):
#     for i in range(44):
#         f2()
#         up()
#         end()
#         delete()
#         space()
#         enter()
#     for i in range(44):
#         up()
#     right()


# Limpador de Série 3
for i in range(12):
    for i in range(44):
        f2()
        up()
        up()
        up()
        home()
        delete()
        delete()
        delete()
        delete()
        end()
        delete()
        enter()
    for i in range(44):
        up()
    right()

right()
right()
right()

for i in range(12):
    for i in range(44):
        f2()
        up()
        up()
        up()
        home()
        delete()
        delete()
        delete()
        delete()
        end()
        delete()
        enter()
    for i in range(44):
        up()
    right()