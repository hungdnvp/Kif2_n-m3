import pyautogui, time

delay = 1
so_lan_click = 10

for i in range(5,0,-1):
    print(i)
    time.sleep(1)

x,y = pyautogui.position()
for i in range(so_lan_click):
    pyautogui.click(x,y)
    time.sleep(delay)