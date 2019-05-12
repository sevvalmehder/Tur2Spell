
import time
from  tkinter import*
import tkinter as tk


def create_ovalq1(canvas, text, x_0, y_0, x_1, y_1, color="SeaGreen3", width=0.0 ,ocolor="SeaGreen" ):
    canvas.create_oval(x_0, y_0, x_1, y_1, fill=color, width=width,  outline=ocolor )
    canvas.create_text(x_0 + 20, y_0 + 20, text=text)
def main_graph(canvas, current_state):

    x0 = 50
    y0 = 400
    # reject
    if current_state=='reject':
        create_ovalq1(canvas, 'reject', x0 + 600, y0 + 150 + 30, x0 + 600 + 40, y0 + 150 + 30 + 40, color="MediumPurple1", width=10, ocolor="gold")
    else:
        create_ovalq1(canvas, 'reject', x0 + 600, y0 + 150 + 30, x0 + 600 + 40, y0 + 150 + 30 + 40,
                      color="MediumPurple1")

    canvas.create_line(x0 + 400 + 40, y0 + 30 + 20 + 40, x0 + 600 + 20, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")
    canvas.create_line(x0 + 40, y0 + 30, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")
    canvas.create_line(x0 + 100 + 20, y0 - 80 + 40, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")  # q2
    canvas.create_line(x0 + 100 + 20, y0 + 40, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")  # q1
    canvas.create_line(x0 + 360 + 15, y0 - 60 + 40, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")  # q5
    canvas.create_line(x0 + 540 + 20, y0 - 90 + 40, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")  # q6
    # accept
    if current_state=='accept':
        create_ovalq1(canvas, 'accept', x0 + 800, y0, x0 + 800 + 40, y0 + 40, color='SkyBlue1', width=10, ocolor="gold")
    else:
        create_ovalq1(canvas, 'accept', x0 + 800, y0, x0 + 800 + 40, y0 + 40, color='SkyBlue1')
    # cadet blue
    canvas.create_line(x0 + 480 + 20, y0 - 260 + 40, x0 + 800, y0 + 20, arrow=tk.LAST, fill="cadet blue")  # q7
    canvas.create_line(x0 + 540 + 20, y0 - 90 + 40, x0 + 800, y0 + 10, arrow=tk.LAST, fill="cadet blue")  # q6
    canvas.create_line(x0 + 200 + 20, y0 - 120 + 20, x0 + 800, y0 + 15, arrow=tk.LAST, fill="cadet blue")  # q8
    canvas.create_line(x0 + 360 + 20, y0 - 60 + 20, x0 + 800, y0 + 16, arrow=tk.LAST, fill="cadet blue")  # q5
    canvas.create_line(x0 + 100 + 20, y0 + 15, x0 + 800, y0 + 18, arrow=tk.LAST, fill="cadet blue")  # q1
    canvas.create_line(x0 + 100 + 20, y0 + 70 + 20, x0 + 800, y0 + 25, arrow=tk.LAST, fill="cadet blue")  # q3
    # q0
    if current_state=='q0':
        create_ovalq1(canvas, 'q0', x0, y0, x0 + 40, y0 + 40, color='blue', width=10, ocolor="gold")
    else:
        create_ovalq1(canvas, 'q0', x0, y0, x0 + 40, y0 + 40, color='blue')
    # line
    shapes = []
    x1 = x0 + 100
    dm = 30
    canvas.create_line(x0 + 40, y0 + 20, x1, y0 - 65, arrow=tk.LAST, fill="SteelBlue1")  # up
    canvas.create_line(x0 + 40, y0 + 20, x1, y0 + 15, arrow=tk.LAST, fill="SteelBlue1")  # direct
    # q2
    if current_state == 'q2':
        create_ovalq1(canvas, 'q2', x0 + 100, y0 - 80, x0 + 100 + 40, y0 - 80 + 40, width=10, ocolor="gold")
    else:
        create_ovalq1(canvas, 'q2', x0 + 100, y0 - 80, x0 + 100 + 40, y0 - 80 + 40)
    canvas.create_line(x0 + 100 + 20, y0 - 40, x0 + 100 + 20, y0, arrow=tk.LAST, fill="SteelBlue1")  # direct

    # q1
    if current_state == 'q1':
        create_ovalq1(canvas, 'q1', x0 + 100, y0, x0 + 100 + 40, y0 + 40, color="chocolate1", width=10, ocolor="gold")
    else:
        create_ovalq1(canvas, 'q1', x0 + 100, y0, x0 + 100 + 40, y0 + 40, color="chocolate1")
    canvas.create_line(x0 + 100 + 20, y0 + 40, x0 + 100 + 20, y0 + 70, arrow=tk.LAST, fill="SteelBlue1")  # direct
    # q3
    if current_state == 'q3':
        create_ovalq1(canvas, 'q3', x0 + 100, y0 + 70, x0 + 100 + 40, y0 + 70 + 40, color="red", width=10, ocolor="gold")
    else:
        create_ovalq1(canvas, 'q3', x0 + 100, y0 + 70, x0 + 100 + 40, y0 + 70 + 40, color="red")
    # q3->>>>q8
    canvas.create_line(x0 + 100 + 30, y0 + 70, x0 + 200 + 10, y0 - 80, arrow=tk.LAST, fill="SteelBlue1")  # up
    # q3->>>>q4
    canvas.create_line(x0 + 100 + 40, y0 + 80, x0 + 400, y0 + 90, arrow=tk.LAST, fill="SteelBlue1")
    # q8 oval
    create_ovalq1(canvas, 'q8', x0 + 200, y0 - 120, x0 + 200 + 40, y0 - 120 + 40, color="yellow3")
    # q8--->q5
    canvas.create_line(x0 + 200 + 30, y0 - 120 + 40, x0 + 360, y0 - 60 + 20, arrow=tk.LAST, fill="SteelBlue1")
    # q8--->q4
    # q8--->q5
    canvas.create_line(x0 + 200 + 30, y0 - 120 + 40, x0 + 400, y0 + 70, arrow=tk.LAST, fill="SteelBlue1")
    # q4

    if current_state == 'q4':
        create_ovalq1(canvas, 'q4', x0 + 400, y0 + 30 + 30, x0 + 400 + 40, y0 + 70 + 30, color="slate blue", width=10,
                      ocolor="gold")
    else:
        create_ovalq1(canvas, 'q4', x0 + 400, y0 + 30 + 30, x0 + 400 + 40, y0 + 70 + 30, color="slate blue")
    # q4--->q5
    canvas.create_line(x0 + 400 + 20, y0 + 70 - 10, x0 + 400, y0 - 60 + 30, arrow=tk.LAST, fill="SteelBlue1")
    # q5
    if current_state == 'q5':
        create_ovalq1(canvas, 'q5', x0 + 360, y0 - 60, x0 + 360 + 40, y0 - 60 + 40, color="brown", width=10,
                      ocolor="gold")
    else:
        create_ovalq1(canvas, 'q5', x0 + 360, y0 - 60, x0 + 360 + 40, y0 - 60 + 40, color="brown")
    # q5---->q6
    canvas.create_line(x0 + 360 + 40, y0 - 60 + 20, x0 + 540, y0 - 70, arrow=tk.LAST, fill="SteelBlue1")

    # q6
    if current_state == 'q6':
        create_ovalq1(canvas, 'q6', x0 + 540, y0 - 90, x0 + 540 + 40, y0 - 90 + 40, color="maroon2", width=10,
                      ocolor="gold")
    else:
        create_ovalq1(canvas, 'q6', x0 + 540, y0 - 90, x0 + 540 + 40, y0 - 90 + 40, color="maroon2")
    # q6--->q7
    canvas.create_line(x0 + 540 + 10, y0 - 90, x0 + 500, y0 - 260 + 40, arrow=tk.LAST, fill="SteelBlue1")
    # q7
    if current_state == 'q6':
        create_ovalq1(canvas, 'q7', x0 + 480, y0 - 260, x0 + 480 + 40, y0 - 260 + 40, color="grey", width=10,
                      ocolor="gold")
    else:
        create_ovalq1(canvas, 'q7', x0 + 480, y0 - 260, x0 + 480 + 40, y0 - 260 + 40, color="grey")
    # q7--->q5
    canvas.create_line(x0 + 480 + 20, y0 - 260 + 40, x0 + 380, y0 - 60, arrow=tk.LAST, fill="SteelBlue1")
    # q7--->q8
    canvas.create_line(x0 + 480 + 20, y0 - 260 + 40, x0 + 200 + 40, y0 - 120 + 20, arrow=tk.LAST, fill="SteelBlue1")

animation = Tk()
canvas = Canvas(animation, width=1000, height=800)
canvas.pack()
state=['q0', 'q1', 'q3', 'q4', 'accept']
for i in range(0, len(state)):
    print(state[i])
    main_graph(canvas, state[i])
    animation.update()
    time.sleep(1)
    canvas.destroy()
    canvas=Canvas(animation, width=1000, height=800)
    canvas.pack()

animation.mainloop()
print("ssssssssssssss")

