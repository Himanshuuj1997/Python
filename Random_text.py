import random
import pyautogui as pg
import time

skills = ('Good Morning','Good Afternoon', 'Good Evening')
time.sleep(10)
for i in range (500):
    a = random.choice(skills)
    pg.write("Hey "+a)
    pg.press('enter')

