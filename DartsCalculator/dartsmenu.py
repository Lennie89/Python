from guizero import *
import subprocess

def OpenN01():
    os.system('dartscalculator.py')

app = App("Darts Menu", width=700, height=500)

n01 = PushButton(app, command=OpenN01(), text="Play 501")

app.display()