import pyautogui
import pygetwindow as gw
import time
import subprocess

# Configurações iniciais
pyautogui.PAUSE = 1  # Pausa padrão para todos os passos

# Abrir Power Automate
pyautogui.press("win")
pyautogui.write("power automate")
pyautogui.press("enter")

# Pausa específica
time.sleep(10)

# Maximizar a janela ativa
window = gw.getActiveWindow()
window.maximize()

# Clicar no botão ENTRAR
pyautogui.click(x=997, y=662)
time.sleep(3)

# Navegar para login
pyautogui.press("tab")  # "outra conta"
pyautogui.press("enter")  # continuar
time.sleep(3)
for _ in range(3):
    pyautogui.press("tab")  # navegando para login
pyautogui.press("enter")  # navegando para login
pyautogui.write("lucaspetry990@gmail.com")  # login com e-mail

# Entrar
for _ in range(2):
    pyautogui.press("tab")  # navegando para entrar
pyautogui.press("enter")  # "entrar"
time.sleep(3)

# Clicar em "meus fluxos"
pyautogui.click(x=123, y=113)
time.sleep(2)

# Fluxo extração e atualização de arquivo MDFE
pyautogui.click(x=63, y=236)  # seleciona o fluxo edge
pyautogui.click(x=225, y=50)  # executa o fluxo "edge"
time.sleep(50)

# Fluxo Power BI
pyautogui.click(x=63, y=236)  # deseleciona o fluxo 1
time.sleep(2)
pyautogui.click(x=64, y=292)  # seleciona o fluxo "2"
pyautogui.click(x=225, y=50)  # executa o fluxo "2"
time.sleep(60)

# Encerra o Power Automate
subprocess.call(["taskkill", "/F", "/IM", "PAD.BrowserNativeMessageHost.exe"])
subprocess.call(["taskkill", "/F", "/IM", "PAD.Console.Host.exe"])

import subprocess
# executa scrit de report WhatsApp
result = subprocess.run(["python", "C:\\Users\\Petry\\Documents\\Py\\B reportWhatsapp.py"], 
capture_output=True, text=True)
print(result.stdout)
print(result.stderr)

