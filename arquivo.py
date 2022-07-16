import pyautogui
import time
print(pyautogui.position())
print(pyautogui.size())
pyautogui.moveTo(106, 372)
print(time.get_clock_info('monotonic'))
time.sleep(3)
pyautogui.click()
time.sleep(3)
pyautogui.alert('Parabéns!')

