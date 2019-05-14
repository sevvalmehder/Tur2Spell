
import time
import sys
from  tkinter import*
import tkinter as tk
from TuringMachine import TuringMachine
input_alphabet = {
        'c': ['b', 'c', 'd', 'g', 'ğ', 'j', 'l', 'm', 'n', 'r', 'v', 'y', 'y', 'z', 'ç', 'f', 'h', 'k', 'p',
                       's', 'ş', 't'],
        'v': ['a', 'ı', 'o', 'u', 'e', 'i', 'ö', 'ü'],
        '#': ['#']
    }
# tape alphabet
tape_alphabet = {
    'c': ['b', 'c', 'd', 'g', 'ğ', 'j', 'l', 'm', 'n', 'r', 'v', 'y',
                   'y', 'z', 'ç', 'f', 'h', 'k', 'p', 's', 'ş', 't'],#consonants = c
    'v': ['a', 'ı', 'o', 'u', 'e', 'i', 'ö', 'ü'],#vowels=v
    '#': ['#'],
    '-': ['-']
}
# set of states
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10'}
# initial state
initial_state = 'q0'
accept_state = 'q9'
reject_state = 'q10'
# Transitions
transitions = {
    # Q0
    'q0': {
        'c': ('q2', 'c', 'R'),
        'v': ('q1', 'v', 'R'),
        '#': (reject_state, '', 'R') #reject
    },
    'q1': {
        'c': ('q3', 'c', 'R'),
        'v': (reject_state, '', 'R'), #reject
        '#': (accept_state, '', 'R')

    },
    'q2': {
        'c': (reject_state, '', 'R'),
        'v': ('q1', 'v', 'R'),
        '#': (reject_state, '', 'R')
    },
    'q3': {
        'c': ('q8', 'c', 'R'),
        'v': ('q4', 'v', 'L'),
        '#': (accept_state, '', 'R') #accept
    },
    'q4': {
        'c': ('q5', tape_alphabet['-'][0]+'c', 'R'),
        'v': (reject_state, '', 'R'),
        '#': (accept_state, '', 'R')
    },
    'q5': {
        'c': (reject_state, '', 'R'),
        'v': ('q6', 'v', 'R'),
        '#': (accept_state, '', 'R')
    },
    'q6': {
        'c': ('q7', 'c', 'R'),
        'v': (reject_state, '', 'R'),
        '#': (accept_state, '', 'R')
    },
    'q7': {
        'c': ('q5', tape_alphabet['-'][0]+'c', 'R'),
        'v': ('q8', 'v', 'L'),
        '#': (accept_state, '', 'R')
    },
     'q8': {
        'c': ('q5', tape_alphabet['-'][0]+'c', 'R'),
        'v': ('q4', 'v', 'L'),
        '#': (accept_state, '', 'R')
    }
}
blank = '#'
#print(transitions)

def create_ovalq1(canvas, text, x_0, y_0, x_1, y_1, color="SeaGreen3", width=0.0 ,ocolor="SeaGreen" ):
    canvas.create_oval(x_0, y_0, x_1, y_1, fill=color, width=width,  outline=ocolor )
    canvas.create_text(x_0 + 20, y_0 + 20, text=text)
def main_graph(canvas, current_state):

    x0 = 500
    y0 = 300
    # reject
    if current_state=='reject':
        create_ovalq1(canvas, 'reject', x0 + 600, y0 + 150 + 30, x0 + 600 + 40, y0 + 150 + 30 + 40, color="MediumPurple1", width=10, ocolor="gold")

    else:
        create_ovalq1(canvas, 'reject', x0 + 600, y0 + 150 + 30, x0 + 600 + 40, y0 + 150 + 30 + 40,
                      color="MediumPurple1")
        canvas.create_rectangle(x0 + 600 + 70, y0 + 150 + 30, x0 + 600 + 40 + 70, y0 + 150 + 30 + 40, fill='red', width=5, outline='tan1')
    canvas.create_line(x0 + 400 + 40, y0 + 30 + 20 + 40, x0 + 600 + 20, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")
    canvas.create_line(x0 + 40, y0 + 30, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")
    canvas.create_line(x0 + 100 + 20, y0 - 80 + 40, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")  # q2
    canvas.create_line(x0 + 100 + 20, y0 + 40, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")  # q1
    canvas.create_line(x0 + 360 + 15, y0 - 60 + 40, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")  # q5
    canvas.create_line(x0 + 540 + 20, y0 - 90 + 40, x0 + 600, y0 + 150 + 30, arrow=tk.LAST, fill="bisque1")  # q6
    # accept
    if current_state=='accept':
        create_ovalq1(canvas, 'accept', x0 + 800, y0, x0 + 800 + 40, y0 + 40, color='SkyBlue1', width=10, ocolor="gold")
        canvas.create_rectangle(x0 + 950, y0, x0 + 1000 + 40+90, y0 + 40, fill='tan1',
                                width=5, outline='tan1')
        canvas.create_text(x0 + 1000 + 20, y0 +30, text='Accepted!')
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
    if current_state == 'q7':
        create_ovalq1(canvas, 'q7', x0 + 480, y0 - 260, x0 + 480 + 40, y0 - 260 + 40, color="grey", width=10,
                      ocolor="gold")
    else:
        create_ovalq1(canvas, 'q7', x0 + 480, y0 - 260, x0 + 480 + 40, y0 - 260 + 40, color="grey")
    # q7--->q5
    canvas.create_line(x0 + 480 + 20, y0 - 260 + 40, x0 + 380, y0 - 60, arrow=tk.LAST, fill="SteelBlue1")
    # q7--->q8
    canvas.create_line(x0 + 480 + 20, y0 - 260 + 40, x0 + 200 + 40, y0 - 120 + 20, arrow=tk.LAST, fill="SteelBlue1")
def create_rects(animation,  pointed_index, input='                      ',):
    canvas = Canvas(animation, width=2000, height=400, bg='lightblue')
    lngt = 50
    width_count=0
    change=0
    current_x=0
    current_y=0
    startpoint=30
    if(len(input)<21):
       startpoint=(2000-(len(input)*lngt))/2
    print("start =", startpoint)
    point_state=0
    for i in range(len(input)):

        current_x = i * lngt+startpoint
        if(i>36 and i<74 ):
            current_x-=37*50
            current_y=125
            point_state=37*50
            canvas.create_rectangle(current_x, current_y, current_x + lngt, current_y + lngt, fill="SkyBlue3", width=3)
            canvas.create_text(current_x + 20, current_y+10, text=input[i])

        if (i >73 and i<80):
            current_x -= 74 * 50
            current_y = 225
            point_state = 74 * 50
            canvas.create_rectangle(current_x, current_y, current_x + lngt, current_y + lngt, fill="SkyBlue3", width=3)
            canvas.create_text(current_x + 20, current_y+10, text=input[i])
        if(i<37):
            current_y=25
            point_state=0
            canvas.create_rectangle(current_x, current_y, current_x + lngt, current_y + lngt, fill="SkyBlue3", width=3)
            canvas.create_text(current_x + 20, 20+current_y, text=input[i])
            #[150,75,225,0,300,75]
            #[spoint, sheigth, mid_width, mid_start, lastpoinX, laspointY]
        print(current_x ,"=", current_y)
        #points = [0,30,22,0,44,30]
        triangle_x=(pointed_index*50+startpoint)-point_state
        if i==pointed_index:
            points = [triangle_x,30+current_y+50,triangle_x+22,current_y+50+0, triangle_x+44,current_y+30+50]
            canvas.create_polygon(points, outline='yellow',
                             fill='DodgerBlue2', width=3)
        canvas.pack()
    return canvas

state=['q0', 'q1', 'q3', 'q4', 'accept']
#canvas.create_rectangle()
'''for i in range(0, len(state)):
    print(state[i])
    main_graph(canvas, state[i])
    animation.update()
    time.sleep(1)

    if i!=len(state)-1:
        canvas.destroy()
        table.destroy()
        canvas = Canvas(animation, width=2000, height=600, bg='white')

        canvas.pack()
        table = create_rects(animation, state, 0)
'''
def gui_execute(animation, input):
    spelling_turing_machine = TuringMachine(states, input_alphabet, tape_alphabet, blank, transitions, initial_state,
                                            accept_state, reject_state)


    output_tape, result, steps = spelling_turing_machine.execute(input)


    i = 0
    for (key, value) in steps:
        if (i == 0):
            canvas = Canvas(animation, width=2000, height=600, bg='white')
            canvas.pack()
            main_graph(canvas, key)

            table = create_rects(animation, value, input)
            animation.update()
            time.sleep(1)
        else:
            print(key, value)
            main_graph(canvas, key)
            animation.update()
            time.sleep(1)

        if i != len(steps) - 1 and i != 0:
            canvas.destroy()
            table.destroy()
            canvas = Canvas(animation, width=2000, height=600, bg='white')

            # time.sleep(1)
            canvas.pack()

            table = create_rects(animation, value, input)
            animation.update()

        i += 1

def tr_input():
    canvas.destroy()
    table.destroy()
    gui_execute(animation, turing_input.get())
    return
animation = Tk()
animation.title('Tur2Spell')
turing_input=StringVar()
inputt = Canvas(animation, width=2000, height=100, bg='LightBlue3')

mLabel=Label(inputt, text="Enter a word").pack()  # this is placed in 0 0

# 'Entry' is used to display the input-field
mEntry=Entry(inputt, textvariable=turing_input).pack()  # this is placed in 0 1
mButton=Button(inputt, text="Turing Machine", command= tr_input, fg="tan2").pack()
inputt.pack()
animation.update()
print(turing_input.get())

canvas = Canvas(animation, width=2000, height=600, bg='white')
canvas.pack()
main_graph(canvas, ' ')
print('sdcdcfdcfdcccccccccccccccccccccccccccccccc')
canvas.pack()
table = create_rects(animation, -1, '          ')
animation.update()
animation.mainloop()
print("ssssssssssssss")

