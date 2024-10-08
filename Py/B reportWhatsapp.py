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

pyautogui.sleep(10)

subprocess.call(["taskkill", "/F", "/IM", "PAD.BrowserNativeMessageHost.exe"])
subprocess.call(["taskkill", "/F", "/IM", "PAD.Console.Host.exe"])