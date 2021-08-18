import pyautogui as pag
x,y=pag.position()
print(x,y)

pag.moveTo(1000,500)
pag.click(1000,500,button='left')
