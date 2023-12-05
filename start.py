import pyautogui
import time

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('cmd')
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('node -v')
pyautogui.press('enter')